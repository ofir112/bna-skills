# BNA Skills — סקילים ל-Claude Code בעברית

חבילת סקילים ל-[Claude Code](https://claude.com/claude-code) מבית *BNA AI (אופיר אשר)*.
מטרה: לתת לקהל הישראלי כלים מוכנים שמרחיבים את היכולות של Claude Code, בעברית ומהבסיס.

## הסקילים בחבילה

| סקיל | מה הוא עושה |
|------|------------|
| `bna-seo` | קידום אתרים בגוגל (SEO) עם תמיכה מלאה בעברית, RTL ושוק ישראלי — מטא תגיות, structured data, sitemap, hreflang ועוד. |
| `bna-performance` | זירוז אתרים ושיפור מהירות טעינה, עם סעיף ייעודי לפונטים בעברית — Core Web Vitals, תמונות, JavaScript, caching ועוד. |
| `bna-tax` | הבנת דוחות מס ישראליים: דוח שנתי, נקודות זיכוי, הוצאות מוכרות, מקדמות והכנה לפגישה עם רואה החשבון. בנוי על עקרון "אימות לפני כל מספר" מול מקורות רשמיים. |
| `bna-mortgage` | השוואת משכנתאות בישראל: הסבר המסלולים בשפה פשוטה, השוואת הצעות בנקים עם חישובים בקוד (לא בראש), תרחישי קיצון, ופלייבוק משא ומתן מול הבנקים. |
| `bna-property-check` | בדיקות לפני קניית דירה: פענוח נסח טאבו סעיף-סעיף, דגלים אדומים, חריגות בנייה, בית משותף, בדק בית וצ'ק-ליסט שאלות לכל הגורמים. |
| `bna-realestate-tax` | מיסוי נדל"ן: מס רכישה, מס שבח ושלושת מסלולי המס על הכנסות משכירות - הבחירה שרוב המשכירים לא יודעים שיש להם. |
| `bna-deal-analyzer` | ניתוח עסקת השקעה במספרים: עלות אמיתית, תשואה נטו, תזרים מול משכנתא, תרחישי קיצון ו-ROE - כל החישובים בקוד. |
| `bna-market-research` | מחקר שוק מעסקאות אמת: שליפת מחירים שנסגרו בפועל מהמאגר הממשלתי והשוואה הוגנת מול המחיר המבוקש. |
| `bna-rent` | שכירות חכמה: ניתוח חוזה עם רמזור סעיפים ונוסח חלופי, פרוטוקול כניסה, מכתבים לבעל הבית והחזרת פיקדון. |
| `bna-listing-pro` | שיווק נכסים לאנשי נדל"ן: תיאורים ומודעות לכל פלטפורמה, הנחיות צילום, מותג אישי ותסריטי מעקב - אמת בפרסום בלבד. |
| `bna-payslip` | פענוח תלוש שכר: כל שורה בעברית פשוטה, צ'ק-ליסט "האם מפרישים לי נכון", דגלים אדומים, ברוטו-נטו בקוד והשוואת הצעות עבודה. |
| `bna-pension` | הדוח השנתי של הפנסיה בעברית של בני אדם, ומחשבון בקוד שמראה כמה דמי הניהול עולים לאורך 30 שנה - בשקלים. |
| `bna-vat` | עוסק פטור או מורשה? השוואה בקוד על המספרים שלך, שלושת המסמכים, דיווחים, קיזוז תשומות וחשבוניות ישראל. |
| `bna-bituach-leumi` | ביטוח לאומי לעצמאים: למה מקדמות נמוכות שוחקות דמי לידה ומילואים, מה מכוסה ומה לא, פנסיה חובה וטיפול בחובות. |
| `bna-car` | קניית רכב בלי ליפול: בדיקות חובה ליד שנייה, מזומן מול מימון מול ליסינג בקוד, ריבית אפקטיבית אמיתית ודגלים אדומים. |
| `bna-miluim` | זכויות מילואים בבדיקה חיה מול המקורות הרשמיים: תגמולים, מענקים, הגנות בעבודה, סטודנטים והגשת תביעות. |
| `bna-video-ad` | פרסומת וידאו מציאותית לכל עסק בהיגספילד, מפרומפט בלבד: 6 שאלות קצרות, 3 רמות איכות עם מחיר מדויק בקרדיטים (Seedance 2.5, Kling 3.0, Seedance 2.0 Mini), 2 גרסאות לבחירה, מוזיקה וכרטיס סיום בעברית. |

## התקנה מהירה

הדביקו את השורה הבאה בתוך Claude Code והוא יתקין את הסקיל אוטומטית:

```bash
curl -sL https://github.com/ofir112/bna-skills/archive/main.tar.gz | tar -xz -C /tmp && cp -r /tmp/bna-skills-main/skills/bna-seo ~/.claude/skills/ && rm -rf /tmp/bna-skills-main
```

זהו. עכשיו כשתבקשו מ-Claude "תשפר לי את ה-SEO של הדף" או "תקן לי את המטא תגיות" — הסקיל ייכנס לפעולה לבד.

### התקנת סקיל הביצועים (`bna-performance`)

```bash
curl -sL https://github.com/ofir112/bna-skills/archive/main.tar.gz | tar -xz -C /tmp && cp -r /tmp/bna-skills-main/skills/bna-performance ~/.claude/skills/ && rm -rf /tmp/bna-skills-main
```

עכשיו כשתבקשו "האתר איטי, תזרז אותו" או "תשפר מהירות טעינה" — הסקיל ייכנס לפעולה.

### התקנת סקיל המיסים (`bna-tax`)

```bash
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-tax@bna
```

עכשיו כשתשאלו על "דוח שנתי", "נקודות זיכוי" או "החזר מס" — הסקיל ייכנס לפעולה.
שימו לב: הסקיל עוזר להבין ולהתכונן. הוא לא מגיש דוחות ולא מחליף רואה חשבון.

### התקנת סקיל המשכנתאות (`bna-mortgage`)

```bash
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-mortgage@bna
```

עכשיו כשתשאלו על "תמהיל משכנתא", "השוואת משכנתאות" או "מסלול פריים" — הסקיל ייכנס לפעולה.
שימו לב: הסקיל עוזר להשוות ולהבין. הוא לא ממליץ "קחו את ההצעה הזאת" ולא מחליף יועץ משכנתאות.

### התקנת סקילי הנדל"ן

כל אחד מהסקילים מותקן באותה צורה - מדביקים בתוך Claude Code:

```bash
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-property-check@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-realestate-tax@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-deal-analyzer@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-market-research@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-rent@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-listing-pro@bna
```

כל סקילי הנדל"ן עוזרים להבין, לחשב ולהתכונן - הם לא מחליפים עורך דין מקרקעין, שמאי, יועץ מס או יועץ השקעות.

### התקנת סקילי הכסף האישי והזכויות

```bash
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-payslip@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-pension@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-vat@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-bituach-leumi@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-car@bna
claude plugin marketplace add ofir112/bna-skills && claude plugin install bna-miluim@bna
```

גם כאן: הסקילים עוזרים להבין, לחשב ולהתכונן - הם לא ייעוץ משפטי, פנסיוני, ביטוחי או מס, ולא קובעים זכאות. בכל החלטה מהותית, איש מקצוע מוסמך הוא הכתובת.

### התקנת סקיל הפרסומות (`bna-video-ad`)

הדביקו את השורה הזאת בצ'אט של Claude Code:

```
תתקין לי את סקיל הפרסומות של BNA ותתחיל לעבוד איתו: claude plugin marketplace add ofir112/bna-skills; claude plugin marketplace update bna; claude plugin install bna-video-ad@bna
```

מהפעם הבאה מספיק לכתוב "תיצור לי פרסומת".
צריך חשבון היגספילד עם קרדיטים שמחובר ל-Claude. לפני כל יצירה הסקיל מראה כמה קרדיטים היא תעלה, ולא מוציא כלום בלי אישור.

### התקנת כל הסקילים בבת אחת

```bash
curl -sL https://github.com/ofir112/bna-skills/archive/main.tar.gz | tar -xz -C /tmp && cp -r /tmp/bna-skills-main/skills/* ~/.claude/skills/ && rm -rf /tmp/bna-skills-main
```

## איך יודעים שזה עבד

הריצו בתוך Claude Code:

```bash
ls ~/.claude/skills/
```

אתם אמורים לראות תיקייה בשם `bna-seo`. אפשר גם פשוט לבקש מ-Claude: "אילו סקילים מותקנים אצלי?"

## הסרה

```bash
rm -rf ~/.claude/skills/bna-seo
```

## רישיון

MIT. חלק מהידע ב-`bna-seo` מבוסס על סקילי web-quality פתוחים (MIT), ונכתב מחדש והורחב על ידי BNA AI עם שכבת עברית/RTL וידע מהשוק הישראלי. פרטים ב-[LICENSE](LICENSE).

---

עוד על BNA AI: [Instagram](https://www.instagram.com/ofir.ai/) · [Facebook](https://www.facebook.com/OfirAi)
