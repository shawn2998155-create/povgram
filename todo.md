# POVGram MVP - Development Checklist

## Database & Backend
- [x] Database schema for experiences (videos)
- [x] tRPC procedures: list experiences, search, filter by category
- [x] tRPC procedures: upload experience (with storage integration)
- [x] tRPC procedures: get experience by ID
- [x] tRPC procedures: get related experiences
- [x] Storage integration for video uploads

## Frontend - Layout & Theme
- [x] Dark mode theme configuration (Tailwind + CSS variables)
- [x] Global layout wrapper with navigation
- [x] Neon accent colors and futuristic design tokens
- [x] Mobile-first responsive breakpoints

## Pages & Features
- [x] Homepage with hero section ("Experience life through others' eyes")
- [x] Featured experiences carousel on homepage
- [x] Category navigation (Travel, Events, Jobs, Lifestyle, Extreme)
- [x] Homepage CTAs: "Explore Experiences" and "Upload POV"
- [x] Explore page with search bar
- [x] Explore page with category filters
- [x] Explore page with vertical video card grid
- [x] Experience detail page with vertical video player
- [x] Experience detail page with description, creator, related experiences
- [x] TikTok-style vertical scrolling feed (full-screen)
- [x] Video feed with autoplay and swipe navigation
- [x] Upload page with form (video, title, category, description)
- [x] Auth pages (login/register)

## Video Features
- [x] Video player component (vertical, mobile-optimized)
- [x] POVGram watermark overlay on videos
- [x] Share button per experience
- [x] Lazy loading utilities for videos (lazyLoad.ts)
- [x] Video thumbnail generation helper (generateVideoThumbnail)

## SEO & Performance
- [x] SEO metadata (title, description, OG tags)
- [x] Smooth animations (fade, scale, scroll transitions)
- [x] Mobile responsiveness polish
- [x] Performance optimization utilities (debounce, throttle, caching, batching)

## Testing & Deployment
- [x] Unit tests for key procedures (14 tests passing)
- [x] Deployment guide (Vercel)
- [x] Setup instructions and documentation
- [x] Comprehensive SETUP.md with step-by-step guide

## Comments & Interactions (NEW)
- [x] Database schema for comments (with relationships to experiences and users)
- [x] tRPC procedures: create comment, get comments by experience, delete comment
- [x] Comments component with form and comment list
- [x] Integration into Experience detail page
- [x] Unit tests for comment procedures (6 tests passing)
