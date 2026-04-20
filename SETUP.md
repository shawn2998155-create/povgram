# POVGram - Complete Setup Guide

## Table of Contents

1. [Local Development Setup](#local-development-setup)
2. [Database Configuration](#database-configuration)
3. [Environment Variables](#environment-variables)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Troubleshooting](#troubleshooting)

---

## Local Development Setup

### Prerequisites

Before you begin, ensure you have:

- **Node.js 18+**: Download from [nodejs.org](https://nodejs.org)
- **pnpm**: Install globally with `npm install -g pnpm`
- **Git**: For version control
- **MySQL/TiDB Database**: Local or cloud instance
- **Manus Account**: For OAuth credentials

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd povgram
```

### Step 2: Install Dependencies

```bash
pnpm install
```

This installs all required packages for both frontend and backend.

### Step 3: Set Up Environment Variables

Create a `.env.local` file in the project root:

```bash
cp .env.example .env.local
```

Edit `.env.local` with your credentials (see [Environment Variables](#environment-variables) section).

### Step 4: Database Setup

#### Option A: Using Manus Database (Recommended)

If using Manus-provided database:

```bash
# Generate migrations from schema
pnpm drizzle-kit generate

# Apply migrations
pnpm drizzle-kit migrate
```

#### Option B: Using External MySQL

1. Create a new MySQL database:

```sql
CREATE DATABASE povgram;
```

2. Update `DATABASE_URL` in `.env.local`:

```env
DATABASE_URL=mysql://username:password@localhost:3306/povgram
```

3. Run migrations:

```bash
pnpm drizzle-kit generate
pnpm drizzle-kit migrate
```

### Step 5: Start Development Server

```bash
pnpm dev
```

The application will be available at `http://localhost:3000`.

---

## Database Configuration

### Schema Overview

POVGram uses Drizzle ORM with the following tables:

#### Users Table

```typescript
{
  id: number,                    // Auto-increment primary key
  openId: string,                // Manus OAuth identifier (unique)
  name: string,                  // User's display name
  email: string,                 // User's email
  loginMethod: string,           // OAuth provider (e.g., "manus")
  role: "user" | "admin",        // User role
  createdAt: Date,               // Account creation timestamp
  updatedAt: Date,               // Last update timestamp
  lastSignedIn: Date,            // Last login timestamp
}
```

#### Experiences Table

```typescript
{
  id: number,                    // Auto-increment primary key
  creatorId: number,             // Foreign key to users.id
  title: string,                 // Experience title
  description: string,           // Full description
  category: string,              // One of: Travel, Events, Jobs, Lifestyle, Extreme
  videoUrl: string,              // Storage URL from Manus
  videoKey: string,              // Storage key for reference
  thumbnailUrl: string,          // Optional thumbnail URL
  duration: number,              // Video duration in seconds
  viewCount: number,             // View counter
  createdAt: Date,               // Creation timestamp
  updatedAt: Date,               // Last update timestamp
}
```

### Creating Indexes

For optimal performance, create these indexes:

```sql
CREATE INDEX idx_category ON experiences(category);
CREATE INDEX idx_creatorId ON experiences(creatorId);
CREATE INDEX idx_title ON experiences(title);
CREATE INDEX idx_createdAt ON experiences(createdAt DESC);
```

### Viewing Database

To view your database in development:

```bash
# Using Drizzle Studio (recommended)
pnpm drizzle-kit studio

# Then open http://localhost:5555 in your browser
```

---

## Environment Variables

### Required Variables

Create `.env.local` with these variables:

```env
# Database Connection
DATABASE_URL=mysql://user:password@host:3306/povgram

# Manus OAuth Configuration
VITE_APP_ID=your-app-id-from-manus
OAUTH_SERVER_URL=https://api.manus.im
VITE_OAUTH_PORTAL_URL=https://oauth.manus.im

# JWT Secret (generate a random string)
JWT_SECRET=your-random-jwt-secret-here

# Owner Information
OWNER_OPEN_ID=your-manus-open-id
OWNER_NAME=Your Name

# Manus APIs
BUILT_IN_FORGE_API_URL=https://api.manus.im
BUILT_IN_FORGE_API_KEY=your-api-key
VITE_FRONTEND_FORGE_API_URL=https://api.manus.im
VITE_FRONTEND_FORGE_API_KEY=your-frontend-api-key
```

### Optional Variables

```env
# Analytics (optional)
VITE_ANALYTICS_ENDPOINT=https://your-analytics.com
VITE_ANALYTICS_WEBSITE_ID=your-website-id

# App Branding (optional)
VITE_APP_TITLE=POVGram
VITE_APP_LOGO=https://your-logo-url.com/logo.png
```

### Generating JWT_SECRET

```bash
# On macOS/Linux
openssl rand -base64 32

# On Windows (PowerShell)
[Convert]::ToBase64String((1..32 | ForEach-Object { [byte](Get-Random -Maximum 256) }))
```

---

## Running the Application

### Development Mode

```bash
pnpm dev
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:3000/api/trpc
- Drizzle Studio: http://localhost:5555 (when running `pnpm drizzle-kit studio`)

### Production Build

```bash
# Build the application
pnpm build

# Start production server
pnpm start
```

### Development with Hot Reload

The development server includes:

- **Vite HMR**: Frontend hot module replacement
- **Express Auto-reload**: Backend changes trigger restart
- **TypeScript Checking**: Real-time type checking

---

## Testing

### Running Tests

```bash
# Run all tests
pnpm test

# Run specific test file
pnpm test server/experiences.test.ts

# Watch mode (re-run on file changes)
pnpm test --watch
```

### Test Coverage

Current test coverage:

- ✅ Authentication (logout flow)
- ✅ Experience procedures (list, search, filter, upload, get by ID)
- ✅ Related experiences logic

### Writing New Tests

Create test files with `.test.ts` extension:

```typescript
import { describe, it, expect } from "vitest";
import { appRouter } from "./routers";

describe("my-feature", () => {
  it("should do something", async () => {
    const caller = appRouter.createCaller({ user: null, req, res });
    const result = await caller.myFeature.myProcedure({ input: "test" });
    expect(result).toBe("expected");
  });
});
```

---

## Deployment

### Deploy to Vercel

#### Step 1: Prepare Repository

```bash
# Ensure all changes are committed
git add .
git commit -m "POVGram ready for deployment"
git push origin main
```

#### Step 2: Connect to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will auto-detect the full-stack setup

#### Step 3: Configure Environment Variables

In Vercel dashboard, add all variables from `.env.local`:

- `DATABASE_URL` (production database)
- `VITE_APP_ID`
- `OAUTH_SERVER_URL`
- `JWT_SECRET`
- `OWNER_OPEN_ID`
- `OWNER_NAME`
- `BUILT_IN_FORGE_API_URL`
- `BUILT_IN_FORGE_API_KEY`
- `VITE_FRONTEND_FORGE_API_URL`
- `VITE_FRONTEND_FORGE_API_KEY`
- `VITE_OAUTH_PORTAL_URL`

#### Step 4: Deploy

Click "Deploy" and wait for the build to complete.

#### Step 5: Verify Deployment

- Visit your Vercel URL
- Test all core features:
  - [ ] Homepage loads
  - [ ] Explore page works
  - [ ] Search functionality
  - [ ] Experience detail pages
  - [ ] Video feed
  - [ ] Login/logout
  - [ ] Upload (authenticated)

### Deploy to Other Platforms

POVGram can be deployed to:

- **Railway**: Similar to Vercel, supports full-stack
- **Render**: Full-stack deployment with PostgreSQL
- **AWS**: EC2, Lambda, or ECS
- **DigitalOcean**: App Platform or Droplets
- **Heroku**: Using Procfile (legacy)

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed instructions.

---

## Troubleshooting

### Common Issues

#### 1. Database Connection Error

**Error**: `Error: connect ECONNREFUSED 127.0.0.1:3306`

**Solution**:
- Verify MySQL is running: `mysql -u root -p`
- Check `DATABASE_URL` in `.env.local`
- Ensure database exists: `CREATE DATABASE povgram;`

#### 2. OAuth Login Fails

**Error**: `Invalid OAuth credentials` or redirect loop

**Solution**:
- Verify `VITE_APP_ID` is correct
- Check `OAUTH_SERVER_URL` is accessible
- Ensure redirect URL matches Manus OAuth settings
- Clear browser cookies and try again

#### 3. Videos Not Uploading

**Error**: `Failed to upload video` or `413 Payload Too Large`

**Solution**:
- Check file size (max 100MB)
- Verify video format (MP4 recommended)
- Check storage credentials in `.env.local`
- Ensure `BUILT_IN_FORGE_API_KEY` is valid

#### 4. Search Not Working

**Error**: `No results` or `500 error`

**Solution**:
- Verify database migrations were applied
- Check if experiences exist in database
- Create database indexes (see Database Configuration)
- Check server logs for errors

#### 5. Build Fails on Deployment

**Error**: `Build failed` or `Timeout`

**Solution**:
- Check all environment variables are set
- Verify database connection string
- Increase build timeout in Vercel settings
- Check build logs for specific errors

### Debug Mode

Enable debug logging:

```typescript
// In server code
console.log("[DEBUG]", message);

// In browser console
localStorage.setItem("debug", "povgram:*");
```

### Performance Issues

If the app is slow:

1. Check database query performance
2. Enable caching with `RequestCache`
3. Use lazy loading for videos
4. Optimize images and videos
5. Check Vercel analytics dashboard

### Getting Help

- Check logs: `pnpm dev` output or Vercel dashboard
- Review [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
- Check [README.md](./README.md) for API documentation
- Review test files for usage examples

---

## Next Steps

After setup, consider:

1. **Add sample data**: Upload test experiences
2. **Customize branding**: Update logo and colors
3. **Set up analytics**: Configure analytics endpoint
4. **Enable notifications**: Set up email notifications
5. **Implement moderation**: Add content review system
6. **Add advanced features**: Comments, likes, following

---

## Support

For additional help:

- Review code comments in `client/src/` and `server/`
- Check tRPC documentation: https://trpc.io
- Review Tailwind CSS docs: https://tailwindcss.com
- Manus support: https://help.manus.im

---

**Happy coding! 🚀**
