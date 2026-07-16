---
name: bna-seo
description: Optimize websites for search engine visibility and ranking, with first-class support for Hebrew and RTL sites. Use when asked to "improve SEO", "optimize for search", "fix meta tags", "add structured data", "sitemap", "search engine optimization", "קידום אורגני", "לשפר SEO", "לתקן מטא תגיות", or "לקדם אתר בגוגל".
license: MIT
metadata:
  author: BNA AI (Ofir Asher)
  version: "2.0"
  based-on: web-quality-skills (MIT) — rewritten and extended with Hebrew/RTL SEO, Israeli-market guidance, and a workflow-first structure.
---

# BNA SEO — קידום אתרים בגוגל (כולל עברית ו-RTL)

סקיל לאופטימיזציית מנועי חיפוש, בנוי לפי ההנחיות של Google Search ו-Lighthouse SEO.
בניגוד למדריכי SEO גנריים, הסקיל הזה כולל *שכבה ייעודית לאתרים בעברית ו-RTL* ולשוק הישראלי — בדיוק המקום שבו רוב הכלים נופלים.

הסקיל נותן לך שני דברים: *סדר עבודה* (workflow) שאומר במה לטפל קודם, ו*ספריית פתרונות* מוכנים להעתקה.

---

## סדר עבודה מומלץ (עבוד לפי הסדר הזה)

אל תתחיל מ-structured data. הסדר הנכון לפי השפעה מול מאמץ:

1. *לוודא שהאתר בכלל נסרק ומאונדקס* — HTTPS, robots.txt, אין `noindex` בטעות, יש sitemap.
2. *On-page על הדפים החשובים* — title ייחודי, meta description, H1 בודד, מבנה כותרות הגיוני.
3. *התאמות עברית/RTL* — `lang`, `dir`, hreflang, מבנה URL בעברית. (ראה סעיף ייעודי למטה.)
4. *מובייל* — viewport, גדלי טקסט וכפתורים.
5. *Structured Data* — סכמות JSON-LD רלוונטיות (Organization, Product, FAQ, Breadcrumbs).
6. *תחזוקה* — Search Console, קישורים שבורים, עדכון sitemap.

מדד עצירה: לפני שממשיכים לשלב הבא, מריצים Lighthouse SEO ובודקים שהציון עלה.

---

## חלוקת המשקל של דירוג בגוגל

| גורם | השפעה מוערכת | מכוסה בסקיל |
|------|--------------|-------------|
| איכות ורלוונטיות תוכן | ~40% | חלקי (מבנה בלבד) |
| קישורים נכנסים וסמכות (backlinks) | ~25% | ✗ (מחוץ לתחום טכני) |
| SEO טכני | ~15% | ✓ |
| חוויית עמוד / Core Web Vitals | ~10% | חלקי |
| On-page SEO | ~10% | ✓ |

*המסקנה המעשית:* אף פעם אל תבטיח לתלמיד או ללקוח "מקום ראשון בגוגל" מטיפולים טכניים בלבד. SEO טכני מסיר חסמים ומאפשר לגוגל לראות את האתר נכון. תוכן טוב וקישורים הם מה שמדרג.

---

## 1. סריקה ואינדוקס (Crawlability)

### robots.txt

```text
# /robots.txt
User-agent: *
Allow: /

# חסימת אזורים פרטיים/ניהוליים
Disallow: /admin/
Disallow: /api/
Disallow: /private/

# אל תחסום קבצים שגוגל צריך כדי לרנדר את הדף (CSS/JS)
# ❌ Disallow: /assets/

Sitemap: https://your-domain.co.il/sitemap.xml
```

### מטא robots

```html
<!-- ברירת מחדל: אינדוקס ומעקב קישורים -->
<meta name="robots" content="index, follow">

<!-- למנוע אינדוקס של דף מסוים (תודה, לא) -->
<meta name="robots" content="noindex, nofollow">

<!-- שליטה בתצוגת סניפט בתוצאות -->
<meta name="robots" content="max-snippet:150, max-image-preview:large">
```

*טעות נפוצה:* דף נחיתה עולה לאוויר עם `noindex` שנשאר משלב הפיתוח, וכל הקידום מתבזבז. תמיד לבדוק את זה קודם.

### Canonical

```html
<!-- למנוע כפילות תוכן — כל דף מצביע על עצמו -->
<link rel="canonical" href="https://your-domain.co.il/current-page">
```

---

## 2. On-page SEO

### תגית Title

```html
<!-- ❌ גנרי / חסר -->
<title>דף הבית</title>

<!-- ✅ תיאורי עם מילת המפתח בהתחלה + מותג בסוף -->
<title>נעלי ריצה לנשים | משלוח חינם | שם החנות</title>
```

הנחיות: 50-60 תווים, מילת מפתח ראשית קרוב להתחלה, ייחודי לכל דף, שם המותג בסוף.
*הערה לעברית:* גוגל סופר תווים, ומילים בעברית קצרות מאנגלית. יש לך יותר מקום למסר — נצל אותו.

### Meta Description

```html
<!-- ✅ משכנע, ייחודי, עם קריאה לפעולה -->
<meta name="description" content="נעלי ריצה לנשים במבחר צבעים ומידות. משלוח חינם עד הבית, 30 יום להחזרה. אלפי לקוחות מרוצים. הזמינו עכשיו וקבלו 20% הנחה.">
```

הנחיות: 150-160 תווים, מילת מפתח בטבעיות, קריאה לפעולה, ייחודי לכל דף.

### מבנה כותרות

```html
<!-- ✅ היררכיה נכונה -->
<h1>נעלי ריצה לנשים</h1>
  <h2>מאפייני המוצר</h2>
    <h3>נוחות ובלימת זעזועים</h3>
    <h3>חומרים נושמים</h3>
  <h2>מדריך מידות</h2>
  <h2>ביקורות לקוחות</h2>
```

הנחיות: `<h1>` *אחד בלבד* בעמוד, בלי לדלג רמות, כותרות תיאוריות עם מילות מפתח.

### SEO לתמונות

```html
<!-- ✅ תמונה מותאמת -->
<img src="naaley-ritza-nashim-kachol.webp"
     alt="נעל ריצה לנשים בצבע כחול, מבט צד"
     width="800" height="600" loading="lazy">
```

הנחיות: שם קובץ תיאורי (מותר בעברית, אבל אנגלית-תעתיק בטוח יותר), `alt` שמתאר את התמונה, פורמט WebP/AVIF, `loading="lazy"` לתמונות מתחת לקיפול.

### קישורים פנימיים

```html
<!-- ❌ לא תיאורי -->
<a href="/products">לחצו כאן</a>

<!-- ✅ עוגן תיאורי עם מילות מפתח -->
<a href="/products/naaley-ritza">קולקציית נעלי הריצה לנשים</a>
```

---

## 3. עברית ו-RTL — הסעיף שמדריכים אחרים מדלגים עליו

זה הערך הייחודי של הסקיל הזה. אתרים בעברית מפספסים דירוגים בגלל טעויות שקל לתקן.

### הצהרת שפה וכיווניות

```html
<!-- תמיד להצהיר עברית + כיוון ימין-לשמאל בתגית ה-html -->
<html lang="he" dir="rtl">
```

גוגל משתמש ב-`lang` כדי להתאים את הדף לחיפושים בעברית. בלי זה, הדף עלול להיחשב באנגלית ולאבד רלוונטיות.

### hreflang לאתר דו-לשוני (עברית + אנגלית)

```html
<!-- כל גרסה מצביעה על כל הגרסאות, כולל על עצמה -->
<link rel="alternate" hreflang="he" href="https://your-domain.co.il/">
<link rel="alternate" hreflang="en" href="https://your-domain.co.il/en/">
<link rel="alternate" hreflang="x-default" href="https://your-domain.co.il/">
```

*טעות נפוצה:* גרסה עברית שמצביעה רק על האנגלית, בלי הצבעה עצמית. זה שובר את כל המנגנון.

### מבנה URL בעברית

```
✅ תעתיק לטיני (הכי בטוח, קריא בכל מקום):
https://your-domain.co.il/naaley-ritza-nashim

✅ עברית מקודדת (עובד, אבל מתקבל מכוער כשמעתיקים):
https://your-domain.co.il/נעלי-ריצה-לנשים

❌ פרמטרים בלי משמעות:
https://your-domain.co.il/p?id=12345
```

המלצה: לאתרים ישראליים, *slug בתעתיק לטיני* עם מקפים. קריא, יציב, ולא נשבר בשיתופים בוואטסאפ.

### מיקוד גאוגרפי לישראל

- דומיין `.co.il` נותן אות מיקום חזק לקהל הישראלי.
- לעסק מקומי — להוסיף סכמת `LocalBusiness` (ראה סעיף structured data) עם כתובת ושעות בעברית.
- לרשום את העסק ב-Google Business Profile ולחבר לאתר.

### כיוון טקסט מעורב (עברית + מספרים/אנגלית)

```html
<!-- לעטוף קטע אנגלי בתוך משפט עברי כדי שהכיוון לא יישבר -->
<p>הדגם החדש תומך ב-<bdi>Bluetooth 5.0</bdi> ובטעינה מהירה.</p>
```

---

## 4. מובייל

```html
<!-- viewport רספונסיבי — חובה -->
<meta name="viewport" content="width=device-width, initial-scale=1">
```

```css
/* כפתורים וקישורים בגודל אצבע */
.tap-target { min-height: 48px; min-width: 48px; padding: 12px; }
/* טקסט קריא בלי זום */
body { font-size: 16px; line-height: 1.6; }
```

בישראל רוב התנועה מגיעה ממובייל ומוואטסאפ. גוגל מדרג לפי הגרסה הניידת (mobile-first). אם המובייל לא תקין — הדירוג נפגע גם בדסקטופ.

---

## 5. Structured Data (JSON-LD)

הוסף רק סכמות שרלוונטיות לדף. סכמה לא רלוונטית מזיקה יותר משהיא עוזרת.

### Organization

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "שם העסק",
  "url": "https://your-domain.co.il",
  "logo": "https://your-domain.co.il/logo.png",
  "sameAs": [
    "https://www.instagram.com/your-business/",
    "https://www.facebook.com/your-business"
  ]
}
</script>
```

### Product (מוצר בחנות)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "נעלי ריצה לנשים",
  "description": "נעלי ריצה קלות עם בלימת זעזועים, במבחר צבעים ומידות.",
  "brand": { "@type": "Brand", "name": "שם המותג" },
  "offers": {
    "@type": "Offer",
    "price": "349.00",
    "priceCurrency": "ILS",
    "availability": "https://schema.org/InStock",
    "url": "https://your-domain.co.il/products/naaley-ritza"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "1250"
  }
}
</script>
```

> אם האתר הוא קורס/הדרכה ולא חנות, החליפו את `"@type": "Product"` ב-`"@type": "Course"` והשתמשו ב-`provider` במקום `offers`/`brand`.

### FAQ

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "כמה זמן לוקח המשלוח?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "משלוח חינם עד הבית תוך 3-5 ימי עסקים, עם אפשרות לאיסוף עצמי."
      }
    }
  ]
}
</script>
```

### Breadcrumbs

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "בית", "item": "https://your-domain.co.il" },
    { "@type": "ListItem", "position": 2, "name": "מוצרים", "item": "https://your-domain.co.il/products" },
    { "@type": "ListItem", "position": 3, "name": "נעלי ריצה לנשים", "item": "https://your-domain.co.il/products/naaley-ritza" }
  ]
}
</script>
```

### אימות סכמות
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)

---

## 6. XML Sitemap

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://your-domain.co.il/</loc>
    <lastmod>2026-07-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

הנחיות: עד 50,000 כתובות לקובץ, רק כתובות canonical שאמורות להיות מאונדקסות, לעדכן `lastmod` בכל שינוי תוכן, ולהגיש דרך Google Search Console.

---

## צ׳קליסט אודיט SEO

### קריטי (לבדוק ראשון)
- [ ] HTTPS פעיל
- [ ] robots.txt מאפשר סריקה
- [ ] אין `noindex` בדפים חשובים
- [ ] תגיות title קיימות וייחודיות
- [ ] `<h1>` בודד בכל דף
- [ ] `<html lang="he" dir="rtl">` באתר עברי

### חשוב
- [ ] Meta descriptions קיימות
- [ ] Sitemap הוגש ל-Search Console
- [ ] Canonical מוגדר
- [ ] רספונסיבי במובייל
- [ ] hreflang תקין (אתר דו-לשוני)

### בינוני
- [ ] Structured data רלוונטי
- [ ] אסטרטגיית קישורים פנימיים
- [ ] alt לתמונות
- [ ] URLs תיאוריים
- [ ] פירורי לחם (breadcrumbs)

### שוטף
- [ ] תיקון שגיאות סריקה ב-Search Console
- [ ] עדכון sitemap בשינוי תוכן
- [ ] מעקב אחרי שינויי דירוג
- [ ] בדיקת קישורים שבורים

---

## כלים

| כלי | לְמה |
|-----|------|
| Google Search Console | ניטור אינדוקס ותיקון תקלות |
| Google PageSpeed Insights | ביצועים + Core Web Vitals |
| Rich Results Test | אימות structured data |
| Lighthouse | אודיט SEO מלא |

## מקורות
- [Google Search Central](https://developers.google.com/search)
- [Schema.org](https://schema.org/)

---

*סקיל מאת BNA AI (אופיר אשר). מבוסס על ידע SEO פתוח ברישיון MIT, נכתב מחדש והורחב עם שכבת עברית/RTL וידע מהשוק הישראלי.*
