# POVGram MVP - Deployment & Setup Guide

## Overview

POVGram is a first-person video experience platform built with React 19, Express 4, tRPC 11, Tailwind CSS 4, and Manus OAuth. This guide covers deployment, database setup, and production configuration.

**Tech Stack:**
- **Frontend**: React 19 + Vite + Tailwind CSS 4 + TypeScript
- **Backend**: Express 4 + tRPC 11 + Drizzle ORM
- **Database**: MySQL/TiDB
- **Storage**: Manus Storage (S3-compatible)
- **Auth**: Manus OAuth
- **Deployment**: Vercel (recommended)

---

## Prerequisites

Before deploying, ensure you have:

- Node.js 18+ and pnpm installed
- A Manus account with OAuth credentials
- A MySQL/TiDB database (provided by Manus or external)
- Git repository (for version control)

---

## Local Development Setup

### 1. Clone and Install Dependencies

```bash
git clone <your-repo-url>
cd povgram
pnpm install
```

### 2. Environment Variables

Create a `.env.local` file in the project root with the following variables:

```env
# Database
DATABASE_URL=mysql://user:password@host:3306/povgram

# Manus OAuth
VITE_APP_ID=<your-app-id>
OAUTH_SERVER_URL=https://api.manus.im
VITE_OAUTH_PORTAL_URL=https://oauth.manus.im

# JWT Secret (generate a random string)
JWT_SECRET=<your-random-jwt-secret>

# Owner Info
OWNER_OPEN_ID=<your-open-id>
OWNER_NAME=<your-name>

# Manus APIs
BUILT_IN_FORGE_API_URL=https://api.manus.im
BUILT_IN_FORGE_API_KEY=<your-api-key>
VITE_FRONTEND_FORGE_API_URL=https://api.manus.im
VITE_FRONTEND_FORGE_API_KEY=<your-frontend-api-key>

# Analytics (optional)
VITE_ANALYTICS_ENDPOINT=<your-analytics-endpoint>
VITE_ANALYTICS_WEBSITE_ID=<your-website-id>
```

### 3. Database Setup

```bash
# Generate migrations from schema
pnpm drizzle-kit generate

# Apply migrations to database
pnpm drizzle-kit migrate
```

The database schema includes:
- **users**: OAuth user data with role-based access
- **experiences**: POV video metadata (title, category, creator, storage URL, view count)

### 4. Run Development Server

```bash
pnpm dev
```

The app will be available at `http://localhost:3000`.

---

## Deployment to Vercel

### 1. Prepare for Deployment

```bash
# Build the full-stack application
pnpm build

# Test production build locally
pnpm start
```

### 2. Push to GitHub

```bash
git add .
git commit -m "POVGram MVP ready for deployment"
git push origin main
```

### 3. Deploy to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will auto-detect the full-stack setup
5. Configure environment variables in Vercel dashboard:
   - `DATABASE_URL`: MySQL connection string for production
   - `VITE_APP_ID`: Manus OAuth app ID
   - `OAUTH_SERVER_URL`: https://api.manus.im
   - `JWT_SECRET`: Random secure string
   - `OWNER_OPEN_ID`: Your Manus OAuth ID
   - `OWNER_NAME`: Your name
   - `BUILT_IN_FORGE_API_URL`: https://api.manus.im
   - `BUILT_IN_FORGE_API_KEY`: Your Manus API key
   - `VITE_FRONTEND_FORGE_API_URL`: https://api.manus.im
   - `VITE_FRONTEND_FORGE_API_KEY`: Your frontend API key
   - `VITE_OAUTH_PORTAL_URL`: https://oauth.manus.im

6. Click "Deploy"

### 4. Post-Deployment

- Verify the deployment at your Vercel URL
- Test all core features:
  - Homepage loads with hero section
  - Explore page search works
  - Experience detail pages render
  - Video feed scrolls
  - Upload requires authentication
  - Login/logout works
- Monitor logs in Vercel dashboard
- Check database connectivity

---

## Database Configuration

### MySQL/TiDB Setup

POVGram uses Drizzle ORM with MySQL. The schema includes:

- **users**: OAuth user data
- **experiences**: POV video metadata

### Schema Overview

The Drizzle ORM schema is defined in `drizzle/schema.ts`:

**Users Table:**
- `id`: Primary key
- `openId`: Manus OAuth identifier (unique)
- `name`, `email`: User profile data
- `role`: 'user' or 'admin'
- `createdAt`, `updatedAt`, `lastSignedIn`: Timestamps

**Experiences Table:**
- `id`: Primary key
- `creatorId`: Foreign key to users
- `title`: Experience title (required)
- `description`: Full description
- `category`: One of Travel, Events, Jobs, Lifestyle, Extreme
- `videoUrl`: Storage URL from Manus
- `videoKey`: Storage key for reference
- `duration`: Video duration in seconds
- `viewCount`: Engagement metric
- `createdAt`, `updatedAt`: Timestamps

**Recommended Indexes:**
```sql
CREATE INDEX idx_category ON experiences(category);
CREATE INDEX idx_creatorId ON experiences(creatorId);
CREATE INDEX idx_title ON experiences(title);
CREATE INDEX idx_createdAt ON experiences(createdAt DESC);
```

---

## File Storage (Manus Storage)

POVGram uses Manus Storage (S3-compatible) for video uploads. The `storagePut` helper in `server/storage.ts` handles uploads:

```typescript
import { storagePut } from "./server/storage";

// Upload video to storage
const { url, key } = await storagePut(
  `videos/${userId}-${Date.now()}.mp4`,
  videoBuffer,
  "video/mp4"
);

// url: /manus-storage/{key} (use directly in frontend)
// key: storage reference (save in database)
```

**Key Points:**
- Videos are served via `/manus-storage/` path with CDN caching
- Store the `key` in database, use `url` in frontend
- Max file size: 100MB (enforced in upload form)
- Supported formats: MP4, WebM, and other video types
- No manual URL signing needed - Manus handles authentication

---

## Authentication (Manus OAuth)

### How It Works

1. User clicks "Sign In" → redirected to Manus OAuth portal
2. User authenticates and grants permission
3. Manus redirects to `/api/oauth/callback` with authorization code
4. Backend exchanges code for user data and creates/updates user in database
5. Session cookie (JWT) is set with `JWT_SECRET`
6. User is logged in and can access protected features

### Frontend Auth Flow

```typescript
import { useAuth } from "@/_core/hooks/useAuth";
import { getLoginUrl } from "@/const";

// Get current user
const { user, isAuthenticated } = useAuth();

// Redirect to login
window.location.href = getLoginUrl();

// Logout
await trpc.auth.logout.useMutation();
```

### Backend Protected Routes

Use `protectedProcedure` in tRPC to require authentication:

```typescript
experiences: router({
  upload: protectedProcedure
    .input(uploadSchema)
    .mutation(async ({ input, ctx }) => {
      // ctx.user is guaranteed to exist
      return createExperience({
        creatorId: ctx.user.id,
        ...input,
      });
    }),
}),
```

### Session Management

- Sessions are stored as HTTP-only cookies
- JWT_SECRET signs session tokens
- Cookie expires after inactivity
- Logout clears the session cookie

---

## Performance Optimization

### 1. Video Lazy Loading

Videos are lazy-loaded on the Explore and Feed pages to reduce initial load time.

### 2. Database Indexing

Ensure indexes are created for frequently queried columns:

```sql
CREATE INDEX idx_category ON experiences(category);
CREATE INDEX idx_creatorId ON experiences(creatorId);
CREATE INDEX idx_title ON experiences(title);
```

### 3. CDN & Caching

- Videos are served from Manus storage with CDN caching
- Static assets are cached by Vercel
- API responses are cached where appropriate

---

## Monitoring & Maintenance

### Logs

- **Server logs**: Check Vercel dashboard for errors
- **Database logs**: Monitor your database provider's logs
- **Client errors**: Use browser DevTools console

### Common Issues

| Issue | Solution |
|-------|----------|
| 500 error on upload | Check `DATABASE_URL` and storage credentials |
| Videos not playing | Verify video format (MP4 recommended) |
| Search not working | Ensure database indexes are created |
| Auth failures | Verify OAuth credentials in environment |

---

## Future Enhancements

- [ ] Video thumbnail generation
- [ ] Advanced search with Elasticsearch
- [ ] Real-time notifications
- [ ] Creator profiles and following
- [ ] Comments and interactions
- [ ] Monetization features
- [ ] Mobile app (React Native)
- [ ] Live streaming POV

---

## Support & Troubleshooting

For issues or questions:

1. Check logs in Vercel dashboard
2. Review environment variables
3. Test database connection
4. Verify OAuth credentials
5. Contact Manus support for infrastructure issues

---

## Security Considerations

- **Never commit `.env.local`** - add to `.gitignore`
- **Rotate JWT_SECRET** regularly in production
- **Enable HTTPS** (automatic with Vercel)
- **Validate all inputs** with Zod schemas on both client and server
- **Use rate limiting** for API endpoints (consider Vercel middleware)
- **Keep dependencies updated** with `pnpm update`
- **Protect admin procedures** with role checks
- **Use environment-specific secrets** for dev vs production
- **Monitor database access** and logs
- **Implement CORS** if serving from different domain

---

## License

POVGram is built with Manus and uses Manus OAuth for authentication.
