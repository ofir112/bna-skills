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
