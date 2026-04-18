# POVGram - Experience Platform MVP

**Experience life through others' eyes.**

POVGram is a mobile-first platform where users discover and share first-person video experiences. From travel adventures to extreme sports, job shadowing to lifestyle moments – explore real-world perspectives from creators worldwide.

---

## Features

### Core Features (MVP)

- **🎬 Experience Discovery**: Search and explore POV videos by category or keyword
- **📱 Vertical Video Feed**: TikTok-style full-screen scrolling with smooth navigation
- **🎥 Video Upload**: Authenticated users can upload their POV experiences
- **🔍 Smart Search**: Find experiences by title, location, activity, or event
- **📂 Category Browsing**: Travel, Events, Jobs, Lifestyle, Extreme
- **👤 User Authentication**: Secure Manus OAuth integration
- **💾 Cloud Storage**: Videos stored securely with CDN delivery
- **🎨 Dark Mode UI**: Futuristic design with neon cyan accents
- **📊 View Tracking**: Track experience popularity and engagement

### Technical Stack

- **Frontend**: React 19 + Tailwind CSS 4 + TypeScript
- **Backend**: Express 4 + tRPC 11 + Drizzle ORM
- **Database**: MySQL/TiDB
- **Storage**: Manus Storage (S3-compatible)
- **Auth**: Manus OAuth
- **Deployment**: Vercel (recommended)
- **Testing**: Vitest

---

## Project Structure

```
povgram/
├── client/
│   ├── src/
│   │   ├── pages/           # Page components
│   │   ├── components/      # Reusable UI components
│   │   ├── lib/             # Utilities and helpers
│   │   ├── App.tsx          # Main router
│   │   └── index.css        # Global styles
│   └── public/              # Static assets
├── server/
│   ├── db.ts                # Database queries
│   ├── routers.ts           # tRPC procedures
│   └── _core/               # Core infrastructure
├── drizzle/
│   ├── schema.ts            # Database schema
│   └── migrations/          # SQL migrations
├── shared/                  # Shared types
├── storage/                 # S3 helpers
└── package.json
```

---

## Quick Start

### Prerequisites

- Node.js 18+
- pnpm
- MySQL database
- Manus OAuth credentials

### Installation

```bash
# Install dependencies
pnpm install

# Set up environment variables
cp .env.example .env.local
# Edit .env.local with your credentials

# Run database migrations
pnpm drizzle-kit generate
pnpm drizzle-kit migrate

# Start development server
pnpm dev
```

Visit `http://localhost:3000` to see the app.

---

## Key Pages

| Page | Route | Description |
|------|-------|-------------|
| Homepage | `/` | Hero section, featured experiences, categories |
| Explore | `/explore` | Search bar, filters, video grid |
| Experience | `/experience/:id` | Video player, details, related content |
| Feed | `/feed` | Full-screen vertical video feed |
| Upload | `/upload` | Upload new POV experience |
| Login | `/login` | Authentication page |

---

## Database Schema

### Users Table

```typescript
{
  id: number,
  openId: string,           // Manus OAuth ID
  name: string,
  email: string,
  role: 'user' | 'admin',
  createdAt: Date,
  updatedAt: Date,
  lastSignedIn: Date
}
```

### Experiences Table

```typescript
{
  id: number,
  creatorId: number,        // User ID
  title: string,            // "POV: Walking in Tokyo at Night"
  description: string,
  category: 'Travel' | 'Events' | 'Jobs' | 'Lifestyle' | 'Extreme',
  videoUrl: string,         // Storage URL
  videoKey: string,         // Storage key
  thumbnailUrl: string,
  duration: number,         // Seconds
  viewCount: number,
  createdAt: Date,
  updatedAt: Date
}
```

---

## API Endpoints (tRPC)

### Public Procedures

```typescript
// List experiences with filters
experiences.list({ category?, limit?, offset? })

// Search experiences
experiences.search({ query, limit? })

// Get single experience
experiences.getById({ id })

// Get related experiences
experiences.getRelated({ experienceId, limit? })

// Get creator's experiences
experiences.getByCreator({ creatorId, limit? })
```

### Protected Procedures

```typescript
// Upload new experience (requires auth)
experiences.upload({ title, description, category, videoData, videoDuration })

// Get current user
auth.me()

// Logout
auth.logout()
```

---

## Development Workflow

### Adding a New Feature

1. **Update Database Schema** (if needed)
   ```bash
   # Edit drizzle/schema.ts
   pnpm drizzle-kit generate
   pnpm drizzle-kit migrate
   ```

2. **Add Database Queries** in `server/db.ts`

3. **Create tRPC Procedures** in `server/routers.ts`

4. **Build UI Components** in `client/src/pages/` or `client/src/components/`

5. **Write Tests** in `server/*.test.ts`

6. **Run Tests**
   ```bash
   pnpm test
   ```

---

## Deployment

### Deploy to Vercel

1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed instructions.

---

## Performance Optimization

- **Lazy Loading**: Videos load on demand
- **Database Indexing**: Optimized queries for search and filtering
- **CDN Caching**: Videos served from edge locations
- **Code Splitting**: Automatic with Vite
- **Image Optimization**: Tailwind CSS utilities

---

## Security

- **OAuth Authentication**: Secure user verification via Manus
- **Protected Routes**: tRPC `protectedProcedure` for auth-required endpoints
- **Input Validation**: Zod schemas for all API inputs
- **HTTPS**: Automatic with Vercel
- **Environment Secrets**: Never commit `.env.local`

---

## Testing

```bash
# Run all tests
pnpm test

# Run specific test file
pnpm test server/experiences.test.ts

# Watch mode
pnpm test --watch
```

---

## Troubleshooting

### Database Connection Error
- Verify `DATABASE_URL` in `.env.local`
- Check database is running and accessible
- Ensure credentials are correct

### OAuth Login Fails
- Verify `VITE_APP_ID` is correct
- Check `OAUTH_SERVER_URL` is accessible
- Ensure redirect URL matches Manus OAuth settings

### Videos Not Uploading
- Check storage credentials
- Verify video format (MP4 recommended)
- Ensure file size < 100MB

### Search Not Working
- Run database migrations
- Create indexes: `CREATE INDEX idx_title ON experiences(title);`

---

## Future Roadmap

- [ ] Creator profiles and following
- [ ] Comments and interactions
- [ ] Live streaming POV
- [ ] Smart glasses integration
- [ ] Advanced analytics
- [ ] Monetization features
- [ ] Mobile app (React Native)
- [ ] AI-powered recommendations

---

## Contributing

POVGram is an MVP project. For improvements:

1. Create a feature branch
2. Make changes and test
3. Submit pull request
4. Code review and merge

---

## License

POVGram is built with Manus infrastructure and uses Manus OAuth for authentication.

---

## Support

For issues, questions, or feedback:

- Check [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for deployment help
- Review logs in Vercel dashboard
- Contact Manus support for infrastructure issues

---

**Built with ❤️ for POV creators and explorers worldwide.**
