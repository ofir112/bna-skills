---
name: bna-performance
description: Optimize web performance for faster loading and better user experience, with special attention to Hebrew fonts and mobile-heavy Israeli traffic. Use when asked to "speed up my site", "optimize performance", "reduce load time", "fix slow loading", "improve page speed", "performance audit", "האתר איטי", "לזרז את האתר", "לשפר מהירות", or "אופטימיזציית ביצועים".
license: MIT
metadata:
  author: BNA AI (Ofir Asher)
  version: "2.0"
  based-on: web-quality-skills (MIT) — rewritten and extended with Hebrew-font performance, Israeli-market guidance, and a workflow-first structure.
---

# BNA Performance — לזרז אתרים (כולל פונטים בעברית)

סקיל לאופטימיזציית ביצועים לאתרים, בנוי לפי אודיטים של Lighthouse ו-Core Web Vitals.
בניגוד למדריכי ביצועים גנריים, הסקיל הזה כולל *סעיף ייעודי לפונטים בעברית* — אחד הגורמים הכי גדולים לאטיות באתרים ישראליים, ומשהו שכמעט אף מדריך לא נוגע בו.

הסקיל נותן לך *סדר עבודה* (במה לטפל קודם) ו*ספריית פתרונות* מוכנים להעתקה.

---

## סדר עבודה מומלץ (עבוד לפי הסדר הזה)

הטעות הכי נפוצה היא להתחיל לתקן לפני שמודדים. הסדר הנכון:

1. *מדוד קודם.* הרץ Lighthouse או PageSpeed Insights על *מובייל* וראה מה הכי איטי. אל תנחש.
2. *טפל ב-LCP* (התמונה/הכותרת הגדולה בראש הדף) — בדרך כלל הניצחון הכי גדול.
3. *טפל בפונטים* — במיוחד פונטים בעברית. (סעיף ייעודי למטה.)
4. *הורד משקל JavaScript* — defer, code splitting, הסרת ספריות מיותרות.
5. *אופטימיזציה לתמונות* — פורמט WebP/AVIF, גדלים רספונסיביים, lazy loading.
6. *Caching* — כדי שביקור חוזר יהיה מיידי.
7. *מדוד שוב.* השווה לפני/אחרי. אם המספר לא השתפר, החזר את השינוי.

*כלל ברזל:* מודדים תמיד על מובייל ועל חיבור סלולרי, לא על מחשב חזק עם סיבים. ככה רוב הקהל בישראל באמת רואה את האתר.

---

## תקציב משאבים (Performance Budget)

יעדים לדף שנטען מהר גם על סלולר:

| משאב | תקציב | למה |
|------|-------|-----|
| משקל דף כולל | < 1.5 MB | נטען ב-~4 שניות על 3G |
| JavaScript (דחוס) | < 300 KB | זמן פענוח והרצה |
| CSS (דחוס) | < 100 KB | חוסם רינדור |
| תמונות מעל הקיפול | < 500 KB | משפיע על LCP |
| פונטים | < 100 KB | מונע טקסט נעלם/קופץ |
| צד שלישי | < 200 KB | latency שאי אפשר לשלוט בו |

---

## פונטים בעברית — הסעיף שחוסך הכי הרבה זמן טעינה

זה הערך הייחודי של הסקיל הזה. פונטים בעברית הם *כבדים במיוחד* כי הם צריכים לכלול את כל האותיות, הניקוד והטעמים. פונט עברי לא מותאם יכול לשקול 200-400KB לבד, ולתקוע את כל טעינת הדף.

### 1. השתמש ב-font-display: swap

מונע "טקסט נעלם" (FOIT) — הטקסט מוצג מיד בפונט מערכת, ומתחלף כשהפונט המותאם נטען.

```css
@font-face {
  font-family: 'Heebo';
  src: url('/fonts/heebo.woff2') format('woff2');
  font-display: swap;   /* הטקסט נראה מיד */
  font-weight: 400;
}
```

### 2. עשה Subset — קח רק את האותיות שאתה צריך

זה השינוי הכי משמעותי. במקום לטעון פונט שתומך בכל השפות, טוען רק את טווח העברית.

```css
@font-face {
  font-family: 'Heebo';
  src: url('/fonts/heebo-hebrew.woff2') format('woff2');
  font-display: swap;
  /* רק אותיות עברית + סימנים בסיסיים — חוסך מאות KB */
  unicode-range: U+0590-05FF, U+FB1D-FB4F, U+0020-007E;
}
```

טיפ: כלים כמו [google-webfonts-helper](https://gwfh.mranftl.com/fonts) או `glyphhanger` מייצרים לך קובץ subset מוכן.

### 3. העדף פורמט WOFF2

הפורמט הדחוס ביותר. תמיד להשתמש בו כברירת מחדל (תמיכה 97%+).

### 4. Preload לפונט הקריטי בלבד

```html
<link rel="preload" href="/fonts/heebo-hebrew.woff2" as="font" type="font/woff2" crossorigin>
```

### 5. שקול פונט מערכת (הכי מהיר — אפס טעינה)

לפעמים הפתרון הכי טוב הוא לא לטעון פונט חיצוני בכלל. מחסנית פונטים עברית של המערכת נטענת מיידית:

```css
body {
  font-family: 'Heebo', 'Assistant', 'Arial Hebrew', 'Segoe UI', system-ui, sans-serif;
}
```

*המלצה מעשית:* פונטים עבריים פופולריים כמו Heebo, Assistant, Rubik ו-Alef נטענים מ-Google Fonts. אם כבר משתמשים בהם, לוודא subset ו-`display=swap` בכתובת: `...&display=swap`.

---

## נתיב הרינדור הקריטי

### תגובת שרת
* *TTFB < 800ms.* זמן עד הבייט הראשון. שרת יעיל, caching, ו-CDN.
* *דחיסה.* Gzip או Brotli לטקסט. Brotli עדיף (15-20% קטן יותר).
* *HTTP/2 או HTTP/3.* מפחית עומס חיבורים.
* *CDN קרוב לישראל.* שרת קצה בקרבת הקהל (אירופה/ישראל) מקצר את זמן התגובה משמעותית לגולשים ישראלים.

### טעינת משאבים

*Preconnect למקורות חיצוניים:*
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

*Preload למשאב הקריטי (תמונת ה-LCP):*
```html
<link rel="preload" href="/hero.webp" as="image" fetchpriority="high">
```

*דחיית CSS לא קריטי:*
```html
<style>/* סגנונות מעל הקיפול, מוטמעים ישירות */</style>

<link rel="preload" href="/styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/styles.css"></noscript>
```

---

## JavaScript

*דחיית סקריפטים לא חיוניים:*
```html
<!-- ❌ חוסם את הפרסור -->
<script src="/app.js"></script>

<!-- ✅ דחוי (מומלץ) -->
<script defer src="/app.js"></script>

<!-- ✅ אסינכרוני (לסקריפטים עצמאיים כמו אנליטיקס) -->
<script async src="/analytics.js"></script>
```

*Code splitting — טען קוד רק כשצריך:*
```javascript
// פיצול לפי ראוט
const Dashboard = lazy(() => import('./Dashboard'));

// פיצול לפי תנאי
if (user.isPremium) {
  const Premium = await import('./PremiumFeatures');
}
```

*Tree shaking — ייבא רק מה שצריך:*
```javascript
// ❌ מייבא את כל הספרייה
import _ from 'lodash';

// ✅ מייבא רק את הפונקציה
import debounce from 'lodash/debounce';
```

---

## תמונות

### בחירת פורמט
| פורמט | מתי | תמיכה |
|-------|-----|-------|
| AVIF | תמונות, דחיסה הכי טובה | 92%+ |
| WebP | תמונות, גיבוי טוב | 97%+ |
| PNG | גרפיקה עם שקיפות | אוניברסלי |
| SVG | אייקונים, לוגו | אוניברסלי |

### תמונות רספונסיביות
```html
<picture>
  <source type="image/avif" srcset="hero-400.avif 400w, hero-800.avif 800w, hero-1200.avif 1200w"
          sizes="(max-width: 600px) 100vw, 50vw">
  <source type="image/webp" srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
          sizes="(max-width: 600px) 100vw, 50vw">
  <img src="hero-800.jpg" width="1200" height="600" alt="תיאור התמונה"
       loading="lazy" decoding="async">
</picture>
```

### עדיפות לתמונת ה-LCP
```html
<!-- תמונה מעל הקיפול: טעינה מיידית ועדיפות גבוהה -->
<img src="hero.webp" fetchpriority="high" loading="eager" decoding="sync" alt="ראשי">

<!-- תמונות מתחת לקיפול: טעינה עצלה -->
<img src="product.webp" loading="lazy" decoding="async" alt="מוצר">
```

*תמיד* לציין `width` ו-`height` על תמונות — זה מונע "קפיצת" תוכן (CLS) בזמן הטעינה.

---

## Caching

### כותרות Cache-Control
```
# HTML (קאש קצר או ללא)
Cache-Control: no-cache, must-revalidate

# קבצים סטטיים עם hash בשם (לא משתנים)
Cache-Control: public, max-age=31536000, immutable

# קבצים סטטיים ללא hash
Cache-Control: public, max-age=86400, stale-while-revalidate=604800
```

הרעיון: ביקור ראשון טוען הכל, ביקור חוזר כמעט מיידי כי הכל כבר בזיכרון הדפדפן.

---

## ביצועי Runtime

*הימנע מ-layout thrashing (קריאה-כתיבה מעורבבות):*
```javascript
// ❌ מכריח חישוב מחדש בכל סיבוב
elements.forEach(el => {
  const h = el.offsetHeight;      // קריאה
  el.style.height = h + 10 + 'px'; // כתיבה
});

// ✅ קודם כל הקריאות, אז כל הכתיבות
const heights = elements.map(el => el.offsetHeight);
elements.forEach((el, i) => { el.style.height = heights[i] + 10 + 'px'; });
```

*Debounce לפעולות יקרות (scroll/resize/חיפוש):*
```javascript
function debounce(fn, delay) {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), delay); };
}
window.addEventListener('scroll', debounce(handleScroll, 100));
```

*רשימות ארוכות — רנדר רק את מה שנראה:*
```css
/* לרשימות מעל ~100 פריטים */
.virtual-list { content-visibility: auto; contain-intrinsic-size: 0 50px; }
```

---

## סקריפטים צד-שלישי (הרוצחים השקטים של ביצועים)

צ׳אט, פיקסלים, וידג׳טים וכפתורי שיתוף מאטים אתרים דרמטית. אסטרטגיות:

*טעינה אסינכרונית:*
```html
<script async src="https://analytics.example.com/script.js"></script>
```

*טעינה רק באינטראקציה (facade) — למשל וידאו יוטיוב:*
```html
<!-- מציג תמונה סטטית, וטוען את הנגן רק בלחיצה -->
<div class="youtube-facade" data-video-id="abc123" onclick="loadYouTube(this)">
  <img src="/thumbnails/abc123.jpg" alt="כותרת הווידאו">
  <button aria-label="נגן וידאו">▶</button>
</div>
```

*טעינת ווידג׳ט רק כשגוללים אליו:*
```javascript
const observer = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    const s = document.createElement('script');
    s.src = 'https://widget.example.com/embed.js';
    document.body.appendChild(s);
    observer.disconnect();
  }
});
observer.observe(document.querySelector('#widget-container'));
```

---

## מדידה

### מדדים מרכזיים (Core Web Vitals)
| מדד | יעד | מה זה |
|-----|-----|-------|
| LCP | < 2.5 שנ׳ | מתי התוכן הראשי מופיע |
| INP | < 200ms | כמה מהר הדף מגיב ללחיצה |
| CLS | < 0.1 | כמה התוכן "קופץ" בטעינה |
| FCP | < 1.8 שנ׳ | מתי מופיע הפיקסל הראשון |
| TBT | < 200ms | כמה זמן המסך תקוע |

### פקודות בדיקה
```bash
# אודיט Lighthouse מלא
npx lighthouse https://example.com --output html --output-path report.html
```
```javascript
// מדידת המדדים האמיתיים בשטח
import { onLCP, onINP, onCLS } from 'web-vitals';
onLCP(console.log);
onINP(console.log);
onCLS(console.log);
```

*כלים מומלצים:* Lighthouse (בתוך כלי הפיתוח של Chrome), [PageSpeed Insights](https://pagespeed.web.dev/), ו-Chrome DevTools בלשונית Performance.

---

*סקיל מאת BNA AI (אופיר אשר). מבוסס על ידע ביצועים פתוח ברישיון MIT, נכתב מחדש והורחב עם שכבת פונטים בעברית וידע מהשוק הישראלי.*
