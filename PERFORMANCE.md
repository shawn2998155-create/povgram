# POVGram Performance Optimization Guide

## Overview

POVGram includes built-in performance utilities to optimize video delivery, reduce API calls, and improve user experience. This guide explains how to use these utilities.

---

## Lazy Loading Videos

### Purpose

Lazy loading defers video loading until they're needed, reducing initial page load time and bandwidth usage.

### Implementation

```typescript
import { setupLazyLoadVideos, setupLazyLoadImages } from "@/lib/lazyLoad";

// In your component
useEffect(() => {
  const observer = setupLazyLoadVideos(".video-container video", {
    threshold: 0.1,
    rootMargin: "50px",
  });

  return () => observer.disconnect();
}, []);
```

### HTML Structure

```html
<!-- Videos will load when they come into view -->
<video
  data-src="https://storage.example.com/video.mp4"
  data-autoplay="true"
  data-pause-out-of-view="true"
  class="lazy-video"
></video>
```

### Options

- `threshold`: Percentage of element visible before loading (0-1)
- `rootMargin`: Pixels around viewport to start loading ("50px")

---

## Debouncing Search Queries

### Purpose

Debouncing limits API calls when users type in search fields, reducing server load.

### Implementation

```typescript
import { debounce } from "@/lib/performance";

const debouncedSearch = debounce((query: string) => {
  setSearchQuery(query);
}, 300); // 300ms delay

const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
  debouncedSearch(e.target.value);
};
```

### Example: Explore Page

The Explore page uses debounced search to reduce API calls:

```typescript
// Search only fires 300ms after user stops typing
<Input
  placeholder="Search experiences..."
  onChange={handleSearch}
  className="flex-1"
/>
```

---

## Throttling Scroll Events

### Purpose

Throttling limits how often scroll handlers fire, improving performance during rapid scrolling.

### Implementation

```typescript
import { throttle } from "@/lib/performance";

const handleScroll = throttle(() => {
  console.log("Scroll event");
}, 100); // Max once per 100ms

window.addEventListener("scroll", handleScroll);
```

---

## Request Caching

### Purpose

Caching stores API responses to avoid duplicate requests within a time window.

### Implementation

```typescript
import { RequestCache } from "@/lib/performance";

const cache = new RequestCache(60); // 60 second TTL

// Store response
cache.set("experiences-travel", data);

// Retrieve from cache
const cached = cache.get("experiences-travel");
if (cached) {
  setResults(cached);
} else {
  // Fetch from API
}
```

### Use Cases

- Category listings (cache for 60 seconds)
- Featured experiences (cache for 5 minutes)
- Creator profiles (cache for 2 minutes)

---

## Request Batching

### Purpose

Batching combines multiple API requests into single calls, reducing network overhead.

### Implementation

```typescript
import { RequestBatcher } from "@/lib/performance";

const batcher = new RequestBatcher(
  async (ids: string[]) => {
    // Fetch multiple experiences in one call
    return await trpc.experiences.getMultiple.query({ ids });
  },
  10, // Batch size
  50   // Batch delay (ms)
);

// Each request is added to batch
const exp1 = await batcher.request("1");
const exp2 = await batcher.request("2");
// Both requests batched into single API call
```

---

## Video Thumbnail Generation

### Purpose

Generate thumbnails from videos for preview cards and featured sections.

### Implementation

```typescript
import { generateVideoThumbnail } from "@/lib/lazyLoad";

// Generate thumbnail at 2 seconds
const thumbnail = await generateVideoThumbnail(
  "https://storage.example.com/video.mp4",
  2
);

// Use in img tag
<img src={thumbnail} alt="Video thumbnail" />;
```

### On Upload

When users upload videos, generate thumbnail server-side:

```typescript
// In upload procedure
const thumbnail = await generateVideoThumbnail(videoUrl, 1);
await db.experiences.update({
  id: experienceId,
  thumbnailUrl: thumbnail,
});
```

---

## Performance Measurement

### Purpose

Measure and log performance of async operations for monitoring.

### Implementation

```typescript
import { measurePerformance } from "@/lib/performance";

const data = await measurePerformance("fetch-experiences", async () => {
  return await trpc.experiences.list.query();
});

// Logs: [Performance] fetch-experiences: 234.56ms
```

---

## Optimal Video Quality Detection

### Purpose

Automatically select video quality based on network speed.

### Implementation

```typescript
import { getOptimalVideoQuality } from "@/lib/performance";

const quality = await getOptimalVideoQuality();
// Returns: "low" | "medium" | "high"

const videoUrl = `https://storage.example.com/video-${quality}.mp4`;
```

### Network Conditions

| Connection | Quality |
|------------|---------|
| slow-2g, 2g | low |
| 3g | medium |
| 4g | high |

---

## Resource Prefetching

### Purpose

Prefetch resources to improve perceived performance.

### Implementation

```typescript
import { prefetchResource } from "@/lib/performance";

// Prefetch next page resources
prefetchResource("/js/feed.js", "script");
prefetchResource("/css/feed.css", "style");
prefetchResource("https://api.example.com/experiences", "fetch");
```

---

## Best Practices

### 1. Debounce Search

Always debounce search inputs to reduce API calls:

```typescript
const debouncedSearch = debounce(handleSearch, 300);
```

### 2. Lazy Load Videos

Use lazy loading for video-heavy pages:

```typescript
setupLazyLoadVideos(".video-container video");
```

### 3. Cache Repeated Queries

Cache results for frequently accessed data:

```typescript
const cache = new RequestCache(60);
```

### 4. Measure Performance

Monitor slow operations:

```typescript
await measurePerformance("operation-name", async () => {
  // Your code
});
```

### 5. Batch Related Requests

Combine multiple requests when possible:

```typescript
const batcher = new RequestBatcher(batchFn);
```

---

## Monitoring Performance

### Browser DevTools

1. Open DevTools (F12)
2. Go to Network tab
3. Filter by requests
4. Check response times

### Performance Logs

Check console for performance measurements:

```
[Performance] fetch-experiences: 234.56ms
[Performance] upload-video: 1234.56ms
```

### Vercel Analytics

Monitor real user metrics in Vercel dashboard:

- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Cumulative Layout Shift (CLS)

---

## Optimization Checklist

- [ ] Debounce search inputs (300ms)
- [ ] Lazy load videos on Explore page
- [ ] Lazy load images in cards
- [ ] Cache category listings (60s)
- [ ] Batch related API calls
- [ ] Measure slow operations
- [ ] Monitor Vercel analytics
- [ ] Test on slow networks (DevTools)
- [ ] Optimize video file sizes
- [ ] Use CDN for static assets

---

## Common Issues

### Videos Loading Too Slowly

- Check video file size (aim for < 10MB)
- Use lazy loading with smaller threshold
- Enable video compression
- Check network connection speed

### Search Feels Sluggish

- Increase debounce delay to 500ms
- Implement request caching
- Limit search results to 20 items
- Add loading indicator

### High API Usage

- Implement request caching
- Use request batching
- Debounce all input fields
- Throttle scroll events

---

## Resources

- [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
- [Web Vitals](https://web.dev/vitals/)
- [Performance API](https://developer.mozilla.org/en-US/docs/Web/API/Performance)
- [Network Information API](https://developer.mozilla.org/en-US/docs/Web/API/Network_Information_API)

---

## Next Steps

1. Review current performance metrics
2. Identify bottlenecks
3. Implement optimizations
4. Measure improvements
5. Monitor in production

---

**Performance is a feature. Optimize continuously! 🚀**
