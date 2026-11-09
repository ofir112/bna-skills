---
name: bna-video-ad
description: Make a realistic video ad (10-20 seconds) for any business, product, service or place in Higgsfield, from a text prompt only, with no source images. The user picks one of three quality levels with exact credit costs (Seedance 2.5 for the most cinematic look, Kling 3.0 Pro for 1080p at a fraction of the price, or Seedance 2.0 Mini as the cheapest, at 720p). It asks a few short questions first, writes a precise multi-shot prompt and runs two versions. It checks them frame by frame, lets the user watch both and choose, then adds music and a Hebrew end card. Use this whenever the user wants an AI-made video ad, commercial or promo, even if they don't name the tools. Trigger phrases include "תיצור לי פרסומת", "פרסומת לעסק שלי", "סרטון פרסומת", "פרסומת וידאו", "סרטון תדמית", "מודעת וידאו", "פרסומת בהיגספילד", "video ad", "commercial" and "promo video". Not for editing footage the user filmed.
---

# Video ad from a prompt (Higgsfield: Seedance 2.5, Kling 3.0 Pro or Seedance 2.0 Mini)

## Why this method

Ads made by animating AI images look like AI. The image model makes everything glossy, oversaturated and "too perfect", and the video inherits that look.

What looks filmed instead is one prompt-only video generation, written the way a cinematographer talks:
- real lenses
- natural light
- muted color
- a handheld camera
- unposed people

One generation can hold several shots. The cast and the place stay consistent across them, because the model makes them together.

The whole method:
1. Ask a few questions.
2. Write one multi-shot prompt.
3. The user picks a quality level, with exact credit costs.
4. Run two versions: cheap drafts on the premium level, two full versions on the cheaper levels.
5. Check them frame by frame.
6. The user watches both and picks one, or asks for changes.
7. On the premium level only, finish the chosen draft in 1080p.
8. Add music and an end card.

Talk to the user in Hebrew (or in their language), in short and simple sentences.
- Use plural forms ("תבחרו", "יש לכם") unless the user clearly writes as a man or a woman; then match them.
- Explain any technical word in a few plain words. In Hebrew:
  - draft = "טיוטה, גרסת ניסיון זולה באיכות נמוכה"
  - 1080p = "איכות מלאה"
  - Seedance = "מודל הווידאו בהיגספילד"
  - PNG = "קובץ תמונה"
- The user never needs to touch a terminal.

Write the prompts for Seedance in English.

## Credits come first

Every generation spends the user's money. Before every paid call, show the exact cost and wait for a clear yes. Never re-run a failed or disappointing generation on your own; explain, and ask first. On the premium level the final is paid separately, so it happens only after the user has watched both drafts and chosen one.

Costs come from the tool itself: send the same params with `get_cost: true`. It is free and generates nothing.

## Three quality levels

The user chooses. Show the exact cost of each level for their length (from `get_cost`), recommend one in a short line, and let them decide. A paid campaign or a hero video points to premium. Testing an idea or an organic post points to the cheaper levels.

| Level | Model | How it runs | 10 s | 15 s | 20 s |
|---|---|---|---|---|---|
| פרימיום | Seedance 2.5, 1080p | 2 drafts at 480p, then only the chosen one in 1080p | 220 | 330 | 440 |
| משתלם | Kling 3.0 Pro, 1080p | 2 full versions, the user picks one | 40 | 60 | not available |
| חסכוני | Seedance 2.0 Mini, 720p | 2 full versions, the user picks one | 20 | 30 | not available |

These are reference prices from Nov 2026, and they change. The cheaper models go up to 15 seconds, so a 20-second ad is premium only; to save, suggest 15 seconds.

**What a real test showed.** The same 10-second bakery prompt was run on all three:

| Level | Result |
|---|---|
| Seedance 2.5 | The most cinematic and natural, and it followed everything. |
| Kling 3.0 Pro | Sharp, real-looking people for about a tenth of the price. But it put a shop sign with gibberish letters on the facade despite "no sign", and it shot the evening scene in daylight. |
| Seedance 2.0 Mini | Followed the prompt closely: evening light, no sign, a natural hand-off. But 720p is visibly softer, and the oven steam looked a little artificial. |

Tell users this honestly when they choose.

Params per level (all fields go inside the tool's `params` object):

```
פרימיום:  model: seedance_2_5, mode: t2v, duration: 10-20, aspect_ratio, generate_audio: true, draft: true, count: 2
          then the chosen one: same params without draft and count, plus draft_job_id and resolution: 1080p
משתלם:    model: kling3_0, mode: pro, sound: on, duration: 10-15, aspect_ratio (9:16 / 16:9 / 1:1), count: 2
          (for Kling, "mode" means quality: std / pro / 4k)
חסכוני:   model: seedance_2_0_mini, resolution: 720p, generate_audio: true, duration: 10-15, aspect_ratio, count: 2
```

Music in Higgsfield adds about 2 credits on any level.

The shots in the result rarely match the planned seconds exactly. In a 10 s test, the plan of 3 / 3 / 4 came out as 3.25 / 2.46 / 4.33. That is fine, but always take the card timing from the real cuts.

## Step 0: check the setup (quietly, before asking anything)

1. **Higgsfield connected?** Look for the Higgsfield tools: `generate_video`, `jobs_wait`, `balance` and `models_explore`.
   - If they are missing, tell the user how to connect, then stop.
   - In the app: claude.ai → Customize → Connectors → Add custom connector. The URL is `https://mcp.higgsfield.ai/mcp`; then sign in to Higgsfield.
   - In a terminal: `claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp`, then sign in through `/mcp`.
2. **Credits and model:**
   - Call `balance`.
   - Call `models_explore` with `action: "get"` for `seedance_2_5`, `kling3_0` and `seedance_2_0_mini`. Confirm each is available and lists the params in the levels table. Offer only the levels whose model the user's plan includes.
   - Higgsfield's tools suggest "Marketing Studio" for ads. This skill deliberately uses the three models above with a plain text prompt, because that is what gives the filmed look. Follow the tool's instructions for folders (`get_preferences`), costs and errors, but not for the choice of model.
3. **FFmpeg** (free editing software; needed only for the editing step): run `ffmpeg -version`.
   - If it is missing, offer to install it: `brew install ffmpeg` on macOS, `winget install Gyan.FFmpeg` on Windows.
   - If the user declines, deliver the clean video at the end. They can add music and text in CapCut.
4. **Workspace:** create `ads/<short-english-slug>/` in the current folder, with `drafts/`, `final/` and `work/` inside.

## Step 1: ask (one message, then wait)

Ask only what the user's first message didn't answer. If an answer is only partial, ask just the missing part. For example, "my café" gives the type but not the name, so ask "מה שם בית הקפה, ומה מיוחד בו?".

The full set:

```
כדי שהפרסומת תצא מדויקת, כמה שאלות קצרות. מה שתדלגו עליו, אבחר בעצמי:

1. מה מפרסמים? שם העסק או המוצר, ומה מיוחד בו במשפט אחד.
2. למי זה מיועד? (למשל: זוגות צעירים, הורים, בעלי עסקים, סטודנטים)
3. איזו תחושה? חמימה ומשפחתית / יוקרתית ושקטה / אנרגטית וצעירה / מקצועית ואמינה
4. איפה זה קורה ומי מופיע? אם יש לכם תמונות של המקום או המוצר האמיתי, גררו 2-3 לחלון הזה. אתאר אותם בפרומפט, כדי שהסרטון ייראה קרוב למציאות.
5. כמה זמן ובאיזה פורמט? 10 / 15 / 20 שניות, אנכי לרילס או רוחבי ליוטיוב. (בתוכנית תקבלו 3 רמות איכות לבחירה, עם המחיר המדויק של כל אחת.)
6. מה בסוף? שם ומשפט קצר על המסך, ומוזיקה (ניצור בהיגספילד / יש לכם קובץ / בלי). אם יש לוגו, גררו את הקובץ לחלון.
```

- **A physical product:** also ask what the packaging looks like (color, material, shape, lid). For many products the packaging is the brand.
- **Defaults for missing answers:** 15 seconds, vertical 9:16, a warm feeling, music generated in Higgsfield. Say in the plan what you chose.
- **Files the user drags into the window** arrive as file paths. Copy them into `work/`.

## Step 2: plan, then approval

Build the ad in your head before you write any prompt.

**One idea.** Choose one simple idea that carries the whole ad. Good shapes:
- "a day from morning to night"
- "before → after"
- "how it's made → how it feels"
- "one person's small moment of joy"

The viewer should feel the benefit, not read about it.

**The special thing must be seen.** Whatever the user said makes them special has to be visible in at least one shot. "Handmade" means hands filling jars in a small workshop. "Bakes everything every morning" means a tray coming out of the oven.

**Shot 1 is the hook.** Something moves in the first second: a curtain opens, coffee pours, a door swings, light changes. For a YouTube ad, which viewers can skip after 5 seconds, also show the product or the brand inside the first 5 seconds.

**Timing that works.** One simple action per shot. The last shot is long, so the end card has time to stay on screen:

| Length | Shots (seconds each) |
|---|---|
| 10 s | 3 shots: 3 / 3 / 4 |
| 15 s | 5 shots: 2.5 / 3 / 3 / 3 / 3.5 |
| 20 s | 7 shots: 2.5 / 2.5 / 3 / 3 / 2.5 / 3 / 3.5 |

A shot with hands near the face (applying a cream, for example) needs at least 3 seconds; otherwise use a texture close-up instead.

**The last shot holds the end card.** Make it calm, wide, and static or very slow. Leave an empty area where the text will sit: the upper third for vertical, the upper half for 16:9 or when there is a logo. That area should be mid-tone, like evening sky, a shaded wall or soft greenery. Never make it white or blown out, because the card's light text must read on it.

**Get the real costs before you show the plan.** All of these checks are free:
- **Premium:** call `get_cost: true` on the draft params (`draft: true`, `count: 2`) and on the 1080p final (same params with `resolution: "1080p"`, without `draft` and `count`).
- **The cheaper levels:** call `get_cost: true` on their params with `count: 2`, for lengths up to 15 seconds.
- **Music:** add it if the user wants it generated.

**Send the plan in Hebrew,** in this order: the plan, the prompt, the cost, and the question last.

```
הנה התוכנית:

*הרעיון:* <שורה אחת>

*השוטים:*
1. 0-3 ש׳: <מה רואים>
2. ...

*בסוף:* <שם> · <משפט>, <מוזיקה>

*חשוב לדעת:* <only if relevant: the place/product is generated from a description, so it will look close to the real one, not identical>

הפרומפט המלא (באנגלית, ככה המודל עובד הכי טוב) שמור בקובץ <path>/PROMPT.md:
<the English prompt in a code block>

*באיזו רמה להריץ?* (מחירים מדויקים מהיגספילד, לסרטון של <N> שניות)
1. *פרימיום, Seedance 2.5:* הכי קולנועי. 2 טיוטות זולות (<X>), ואז רק הנבחרת באיכות מלאה (<Y>). סה״כ <X+Y>.
2. *משתלם, Kling 3.0 Pro:* חד (1080p). 2 גרסאות מלאות לבחירה: <K>. לפעמים מוסיף שלטים או משנה את שעת היום.
3. *חסכוני, Seedance 2.0 Mini:* 2 גרסאות מלאות לבחירה: <M>. איכות 720p, פחות חד.
<מוזיקה: כ-2 קרדיטים.> יש לכם <balance> קרדיטים.

אני ממליץ על <רמה>, כי <סיבה קצרה>. איזו רמה בוחרים?
```

For 20 seconds, show only the premium line and add: "רוצים לחסוך? ב-15 שניות אפשר גם ברמות הזולות". If a model is missing from the user's plan, leave its line out.

## Step 3: write the prompt

Use five blocks, in this order.

**1. Realism header.** Keep it word for word. Change only the first sentence: what the ad is for, and a concrete place. Write "a small café on a Haifa side street", not "a café".

```
A <N>-second live-action commercial for <what>, <where>. Photorealistic documentary-style footage filmed on location with a cinema camera and vintage 35mm lenses: natural light only, true-to-life muted colors, soft contrast, fine film grain, gentle handheld camera, shallow depth of field. Real people with natural skin texture, pores and small imperfections, relaxed unposed body language. It must look like real filmed footage: not CGI, not a 3D render, not glossy, not oversaturated.
```

**2. Cast, once.** Start with "Cast, identical in every shot:".
- Use 3 recurring people at most. Fewer people means more consistent faces.
- Give each one a NAME IN CAPS, age, hair, skin, and one or two clothing items in distinct colors. Clear colors help the model keep people the same.
- People who appear in one shot only (friends, passers-by) can be described inside that shot.
- Children wear everyday modest clothes, like a T-shirt or a cotton dress. Never write swimwear, bath or undressing scenes for children. In testing, a child lifted onto a kitchen counter showed underwear in one draft, and that ruins an ad.

**3. The place or product, once.** Describe concrete materials, colors, shapes and scale, and keep it grounded and plausible; fantasy architecture looks fake.
- **If the user sent photos:** look at them and turn what you see into words, such as the plaster color, the shutters, the counter wood or the jar's glass and lid. Don't pass the photos to the model. Image inputs pull the video toward a photo or render look, and the text route keeps it filmed.
- **Products:** describe them generically and unlabeled ("a small frosted glass jar with a matte white lid, no label"). Never name real brands. The real logo, and a real product photo if the user has one, go on the end card.
- **Remove text from the world:** "No sign on the facade, no menu board, no lettering on windows, cups or packaging." Signs, menus, printed cups and branded machines come out as gibberish letters.

**4. Shots with timestamps.** One line per shot:

```
Shot 1 [0-3s]: <place, time of day>. <framing>. <ONE simple action>. <camera move>.
```

Avoid these. They break first, or they look like AI:
- screens with UI or text
- reading
- typing
- tying laces and other fine hand work
- crowds
- fast sports
- animals doing tricks
- close-ups of chewing
- anyone speaking to camera

For apps and online services, show the life moment the app makes possible rather than the phone.

**5. Sound and text line.** Keep it word for word, and list the natural sounds of your shots:

```
Hard cuts between shots, calm natural pacing. Sound: natural ambience only: <sounds per shot>. No music, no dialogue, no voice-over. No text, no logos, no subtitles, no watermark anywhere on screen.
```

- **No dialogue:** AI lip-sync and Hebrew speech are unreliable, and music sits better when added in the edit.
- **No text:** the model cannot write Hebrew, so all text goes in the edit.

**Words that push the AI look.** Describe how the shot was filmed, not how impressive it is. Avoid:
- luxury, luxurious, epic, stunning, breathtaking
- cinematic masterpiece, hyperrealistic, 8K, ultra detailed
- flawless, dramatic lighting
- for skincare and beauty: radiant, dewy, poreless, youthful glow

If the user asked for "יוקרתי", translate it into materials and pace instead: stone, linen, oak and brass, slow camera moves, quiet moments, a locked-off last shot.

### Shot ideas by business type

Starting points to adapt. Don't copy them blindly.

- **Real estate or a place:**
  - a curtain opens on the view
  - coffee on the balcony
  - a family moment in the kitchen
  - the building from the street at golden hour
  - the pool or garden at sunset
  - dinner with friends at blue hour
  - a dusk wide shot as the windows light up
- **Restaurant, café or bakery:**
  - a tray out of the oven, steam rising
  - a slow pour
  - handing a cup across the counter
  - friends laughing at a table
  - the place at evening, with warm windows
- **Beauty or cosmetics:**
  - hands filling jars in a small workshop (the "handmade" proof)
  - morning window light in a bathroom
  - the texture on a fingertip, close-up
  - a calm moment at the mirror
  - the jar on a stone sill in soft light (unlabeled)
- **Clinic, coach or professional service:**
  - arriving, a little tense
  - a calm conversation, no lip-sync
  - the work itself, simple and safe
  - relief and a real smile
  - a bright establishing shot
- **Fitness or wellness:**
  - stepping out the door at dawn
  - running on a beach path
  - breath and sweat, close-up
  - a group high-five
  - a calm stretch at sunset
- **Food or drink product:**
  - an ingredient, close-up
  - a pour or a splash
  - the first sip, and a reaction
  - sharing with friends outdoors
  - the product on a table in window light
- **App or online service:**
  - the "before" moment, stress
  - the "after", calm or time with family
  - a warm, wide closing shot (no screens)
- **Tourism, hotel or events:**
  - the arrival view reveal
  - a room or terrace detail
  - the experience moment
  - a toast
  - a golden-hour wide shot

### A proven example (20 s real-estate ad, 7 shots)

```
A 20-second live-action real-estate commercial for a new boutique residential building on the Mediterranean coast of Israel. Photorealistic documentary-style footage filmed on location with a cinema camera and vintage 35mm lenses: natural light only, true-to-life muted colors, soft contrast, fine film grain, gentle handheld camera, shallow depth of field. Real people with natural skin texture, pores and small imperfections, relaxed unposed body language. It must look like real filmed footage: not CGI, not a 3D render, not glossy, not oversaturated.

Cast, identical in every shot: NOA, a woman about 32, shoulder-length dark brown wavy hair, olive skin, light freckles, loose white linen shirt. ITAI, a man about 35, short dark hair, short beard, sky-blue linen shirt. Their daughter, about 5, curly brown hair, yellow cotton dress.

The building: 9 storeys, warm off-white stone facade, deep rounded balconies with olive trees and bougainvillea in planters, floor-to-ceiling windows, a wooden pergola and a narrow pool on the roof, standing right behind the beach promenade.

Shot 1 [0-2.5s]: Morning inside the apartment. Close-up of Noa's hand pulling open a sheer linen curtain; soft sunlight pours in and the calm turquoise sea appears through the floor-to-ceiling window. Slow push-in.
Shot 2 [2.5-5s]: Balcony, morning backlight. Handheld medium shot: Noa holds a coffee mug with both hands and leans on the glass railing, the breeze moves her hair, she looks at the sea and smiles to herself.
Shot 3 [5-8s]: Bright kitchen with oak cabinets and a pale stone counter. Itai lifts their daughter onto the counter and she giggles; Noa walks into frame and kisses the girl's head. Candid and natural.
Shot 4 [8-11s]: Exterior at golden hour, from the beach promenade. Wide shot of the building behind palm trees; a jogger and a woman walking a dog pass in the soft-focus foreground. Slow sideways tracking.
Shot 5 [11-13.5s]: Rooftop pool at sunset, camera at water level. Itai swims to the edge, rests his arms on it and looks at the orange sun touching the sea.
Shot 6 [13.5-16.5s]: Blue hour on a large terrace. Noa, Itai and two friends sit around a wooden dinner table under warm string lights; they clink wine glasses and laugh genuinely. Close medium shot.
Shot 7 [16.5-20s]: Dusk, wide static shot from the sand: the whole building with warm light glowing in its windows, small waves rolling onto the beach in the foreground, the sky fading from pink to deep blue.

Hard cuts between shots, calm natural pacing. Sound: natural ambience only: curtain rustle, gulls, soft waves, a coffee sip, a child's giggle, splashing water, glasses clinking, quiet laughter, evening waves. No music, no dialogue, no voice-over. No text, no logos, no subtitles, no watermark anywhere on screen.
```

Save the final prompt, before you send the plan, to `PROMPT.md` in the ad folder.

## Step 4: two versions

Two versions, because every run is random: the same prompt gives a different film each time. Picking the better of two is much safer than betting on one.

Call `generate_video` with the params of the chosen level from the levels table. All fields go inside the tool's `params` object.

**Premium (Seedance 2.5):**

```
model: seedance_2_5
mode: t2v
prompt: <the prompt>
duration: <10 | 15 | 20>
aspect_ratio: 9:16        (16:9 for YouTube, 1:1 for a square post)
generate_audio: true
draft: true
count: 2
```

**Value (Kling 3.0 Pro):**

```
model: kling3_0
mode: pro
sound: on
prompt: <the prompt>
duration: <10 | 15>
aspect_ratio: 9:16
count: 2
```

**Budget (Seedance 2.0 Mini):**

```
model: seedance_2_0_mini
resolution: 720p
generate_audio: true
prompt: <the prompt>
duration: <10 | 15>
aspect_ratio: 9:16
count: 2
```

On the cheaper levels, each version is already at its final quality. There is no draft and nothing more to pay; the user only picks which one to edit.

On Kling, repeat the "no sign" and the time of day inside the shot line itself, for example: "...a plain cream facade with no shop sign, at blue hour...". It follows those better there than in the header.

- **Cost check first.** Call once with `get_cost: true` and confirm the number matches what the user approved. Then call it for real.
- **If `count: 2` is rejected,** make two separate calls instead.
- **If the tool asks something instead of running,** nothing was generated yet. That can be a recommendation, an "adjustments" note, a preset suggestion, or an `unlim_choice` question about free generations. Read it. Ask the user if it touches money or changes the settings, and don't switch to another model or product.
- **On a timeout,** don't resubmit. Check the job IDs first.

Tell the user it takes a few minutes. Poll with `jobs_wait` and the returned job IDs; each call waits up to 15 seconds, so call it again until both jobs finish.

Download each result URL with `curl` to `drafts/draft1.mp4` and `drafts/draft2.mp4`, on every level. Keep both job IDs; on premium they are needed to finish the chosen draft.

### Check both versions frame by frame

Make a contact sheet at 2 frames a second, 10 per row. Use 2 rows for 10 s, 3 for 15 s and 4 for 20 s. Also print where the cuts fall:

```bash
cd ads/<slug>
for n in draft1 draft2; do
  ffmpeg -v error -y -i drafts/$n.mp4 -vf "fps=2,scale=216:-2,tile=10x<ROWS>:padding=4" -frames:v 1 drafts/${n}_sheet.jpg
  echo "$n cuts:"; ffmpeg -hide_banner -i drafts/$n.mp4 -vf "select='gt(scene,0.28)',showinfo" -an -f null - 2>&1 | grep -oE 'pts_time:[0-9.]+' | cut -d: -f2 | tr '\n' ' '; echo
done
```

Expect one cut fewer than the number of shots. In muted footage two similar shots can hide a cut, so if the count is off, read the last cut from the sheet or from the planned timestamps.

Open each sheet image and check:
- **People:** they stay the same across shots.
- **Hands:** fingers and hands look natural.
- **Children:** they are dressed properly in every frame.
- **Text:** there is no gibberish text, sign or fake logo anywhere.
- **Objects:** nothing morphs, melts or appears from nowhere.
- **The brief:** the special thing is visible, and the place or product matches what was asked.
- **The last shot:** it is calm, with a mid-tone empty area for the card.

### The user watches and chooses (a required stop)

This is the most important stop in the whole skill. On premium, the final is the same film as the draft, just sharper: the same people, the same movement and the same cuts. Whatever bothers the user in the draft will still be there after they pay for the final. On the cheaper levels, what they see is already the final.

So the user must actually watch both versions and choose; your frame check and recommendation only help them decide. Never finish a draft or edit a version without the user's explicit choice, even if one is clearly better and even if they approved the total cost earlier.

1. Put both drafts in front of them:
   - open the folder (`open "<folder>"` on macOS, `explorer "<folder>"` on Windows)
   - give the full file paths
   - send the files if you can
2. Send this message (fill in the details, keep it short):

```
2 הטיוטות מוכנות. לפני שמשלמים על האיכות המלאה, תצפו בשתיהן עד הסוף, עם סאונד.

שימו לב: הטיוטות פחות חדות, כי הן באיכות נמוכה. אל תשפטו את החדות, רק את מה שקורה. הגרסה הסופית תהיה *אותו סרטון בדיוק*, רק חד. מה שמפריע לכם עכשיו יישאר גם בה.

מה לבדוק:
1. האנשים: נראים טבעיים, ואותם אנשים לאורך כל הסרטון?
2. ידיים ותנועה: שום דבר מוזר, מעוות או "קופץ"?
3. כיתוב: אין שלטים או אותיות משובשות?
4. המקום או המוצר: מרגיש כמו העסק שלכם?
5. ההרגשה: זה מה שרציתם להגיד?

אני ממליץ על טיוטה <1/2>, כי <סיבה קצרה>. <מה שמצאתי בבדיקה, כולל בעיות>.

מה בוחרים?
• טיוטה 1 באיכות מלאה (<Y> קרדיטים)
• טיוטה 2 באיכות מלאה (<Y> קרדיטים)
• אף אחת, תגידו מה לשנות ואכין 2 טיוטות חדשות (<X> קרדיטים)

את כרטיס הסיום והמוזיקה אפשר לשנות גם אחר כך בלי עלות. את מה שקורה בשוטים אפשר לשנות רק עכשיו.
```

On the cheaper levels, adapt the message:
- open with "2 הגרסאות מוכנות, תצפו בשתיהן עד הסוף, עם סאונד."
- drop the paragraph about soft drafts and the final
- the choice is "גרסה 1 / גרסה 2 / אף אחת" with no extra cost for 1 or 2; "אף אחת" costs a new run at the same level

3. Wait for the choice. If the user asks for changes:
   - turn their words into the one or two prompt edits that fix it
   - show the change
   - ask before running new drafts
   If both drafts are poor, explain what went wrong and suggest the one prompt change that fixes it.

## Step 5: finish in 1080p (premium only)

On the cheaper levels, skip this step: copy the chosen version to `final/raw_1080.mp4` and go to Step 6. The name is kept so the commands stay the same, even when the file is 720p.

Only after the user picked a draft at the stop above. Call `generate_video` with the same params as the draft, minus `draft` and `count`, plus these two:

```
draft_job_id: <the chosen draft's job id>
resolution: 1080p
```

- Check the cost first with `get_cost: true`.
- A draft can be finished within 7 days. The final is billed for the draft's full length.
- Wait with `jobs_wait`, then download the result to `final/raw_1080.mp4`.
- It should be the same film as the draft, with the same cuts. Run the cut check on it to confirm.

## Step 6: edit (music, end card, sound level)

This step needs FFmpeg. If it isn't installed and the user declined it, skip to Step 7 and deliver `raw_1080.mp4`.

### 6a. Music

- **Generate in Higgsfield.** Find a music model with `models_explore` (`type: "audio"`), for example `elevenlabs_music_v2_5` or `suno_music`, whichever this account lists.
  - Set the duration to the video length plus 2. Suno needs a whole number between 15 and 360.
  - Make it instrumental.
  - Use a prompt like: "Instrumental music for a <N>-second <business> commercial. <mood>, <instruments>. Gentle start, warm build, soft resolved ending. No vocals."
  - Check the cost first (about 2 credits), ask, then download it to `work/music.mp3`.
  - It sometimes comes back longer than asked; the mix trims it.
- **The user's own file:** make sure they have the rights to use it.
- **No music:** keep the natural sound at a modest level, so the user can lay their own music on top later. On Instagram, trending audio added in the app often helps reach.

### 6b. End card

The card is a small HTML page that a headless browser (a browser running with no window) turns into a transparent PNG. This route gives perfect Hebrew, real fonts and a soft gradient behind the text.

The card follows the business's look, not any house style:
- If the user has brand colors or a logo, take the text color (`--ink`) and the line color (`--accent`) from them.
- Otherwise use the warm white below.
- Keep the user's exact wording, and put on the card only what the user gave you.

Write `work/card.html`. It is set for vertical 9:16; the comments give the 16:9 values.

```html
<!doctype html>
<html dir="rtl"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Frank+Ruhl+Libre:wght@500&family=Heebo:wght@300&display=block" rel="stylesheet">
<style>
  :root { --w: 1080px; --h: 1920px;      /* 16:9: 1920px and 1080px */
          --top: 320px;                  /* 16:9: 150px */
          --name: 118px;                 /* 16:9: 88px  */
          --tag: 50px;                   /* 16:9: 42px  */
          --logo-h: 140px;               /* 16:9: 100px */
          --ink: #fff8ee;
          --accent: rgba(255,240,215,.9); }
  html, body { margin: 0; width: var(--w); height: var(--h); background: transparent; overflow: hidden; }
  .scrim { position: absolute; inset: 0;
    background: linear-gradient(180deg, rgba(8,10,18,.55) 0%, rgba(8,10,18,.40) 30%, rgba(8,10,18,0) 55%); }
    /* 16:9: linear-gradient(180deg, rgba(8,10,18,.55) 0%, rgba(8,10,18,.42) 40%, rgba(8,10,18,.20) 62%, rgba(8,10,18,0) 78%) */
  .card { position: absolute; left: 0; right: 0; top: var(--top); text-align: center; color: var(--ink);
          text-shadow: 0 2px 28px rgba(0,0,0,.35); }
  .name { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-size: var(--name); line-height: 1.1;
          letter-spacing: .28em; padding-left: .28em; direction: ltr; }
  .name.he { font-family: 'Frank Ruhl Libre', serif; font-weight: 500; font-size: calc(var(--name) * 1.15);
             letter-spacing: .02em; padding-left: 0; direction: rtl; }
  .line { width: 420px; height: 3px; margin: 30px auto 32px;
          background: linear-gradient(90deg, transparent, var(--accent) 30%, var(--accent) 70%, transparent); }
  .tag  { font-family: 'Heebo', sans-serif; font-weight: 300; font-size: var(--tag); letter-spacing: .02em; }
  .logo { display: block; margin: 40px auto 0; max-width: 300px; max-height: var(--logo-h); }
  .logo.plate { background: #fff; padding: 18px 26px; border-radius: 18px; }
</style></head>
<body>
  <div class="scrim"></div>
  <div class="card">
    <div class="name">BRAND</div>   <!-- Hebrew name: class="name he" -->
    <div class="line"></div>
    <div class="tag">משפט קצר אחד</div>
    <!-- <img class="logo" src="logo.png"> -->
  </div>
</body></html>
```

**Adjusting the card:**
- **Position it from the real frame:** before rendering, grab a frame from the middle of the last shot and see where the empty area ends. Set `--top` so the whole card fits inside that area: the name, the line, the tagline and any logo. Leave at least about 80 px clear above the roofline or the subject. A Hebrew name makes the block taller. In testing, a dusk shot whose sky ended at 29% of the height needed `--top: 200px`; the default 320 put the tagline on a chimney.
- **Long names:** Latin names look best spaced out, as above. If a long name overflows the width, lower `--name`.
- **Bright last shot:** if the frame behind the text is bright, strengthen the scrim until the text reads clearly.
- **Empty area at the bottom:** move `.card` down and flip the gradient.
- **Logo** (the user's file, copied to `work/logo.png`):
  - **Background:** if it has a white or solid background (check with `ffprobe` that `pix_fmt` has an alpha channel), or if it is dark and would vanish on the dark scrim, add `class="logo plate"`. The plate puts it on a clean white tile.
  - **Name in the logo:** if the logo already contains the name, remove the `.name` line and let the logo lead, with `--logo-h` around 220px.
- **Product photo:** a real cut-out product photo (a PNG with a transparent background) can sit on the card the same way as the logo. That makes the card the one place the real product appears.

**Find a Chromium-based browser,** in this order:
1. **On macOS:**
   - `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
   - `/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge`
   - `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`
   - also look in `~/Applications`
2. **On Windows:**
   - `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` (Edge comes with every Windows)
3. **None found, but Node is installed:** run `npx -y playwright install chromium` and use the binary it downloads. On macOS that is `~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing`.
4. **Still nothing:** skip the card and deliver the video. Tell the user to add the text in CapCut or Canva.

**Render the card.** W and H are 1080 and 1920 for vertical, 1920 and 1080 for 16:9:

```bash
W=1080; H=1920
"$CHROME" --headless --disable-gpu --hide-scrollbars --default-background-color=00000000 \
  --window-size=$W,$H --virtual-time-budget=6000 \
  --screenshot="$PWD/work/card.png" "file://$PWD/work/card.html"
```

Open `work/card.png` and check that:
- it is W×H
- the background is transparent
- the Hebrew reads in the right order
- the fonts loaded (if they look like plain defaults, re-run with a larger `--virtual-time-budget`)

### 6c. Mix

- `CS` is the card start: the last cut plus 0.6 seconds. The last shot settles first, and then the card fades in.
- `awk` does the arithmetic, so the commands also work in Git Bash on Windows.
- `W` and `H` are the card's size. The video is scaled to them, so a 720p version from the budget level gets the 1080 card cleanly.

```bash
W=1080; H=1920          # 16:9: W=1920; H=1080
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 final/raw_1080.mp4)
CS=<last cut + 0.6>
CD=$(awk "BEGIN{print $D-$CS+0.5}")
FO=$(awk "BEGIN{print $D-1.2}")
```

**With music:**

```bash
ffmpeg -y -i final/raw_1080.mp4 -loop 1 -framerate 24 -t $CD -i work/card.png -i work/music.mp3 -filter_complex "\
[1:v]format=rgba,fade=t=in:st=0:d=0.8:alpha=1,setpts=PTS-STARTPTS+$CS/TB[card];\
[0:v]scale=$W:$H:flags=lanczos,setsar=1[base];\
[base][card]overlay=0:0:eof_action=pass:format=auto,format=yuv420p[v];\
[0:a]volume=3dB,highpass=f=50,aresample=48000[amb];\
[2:a]atrim=0:$D,asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st=$FO:d=1.2,aresample=48000[mus];\
[mus][amb]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
-map "[v]" -map "[a]" -t $D -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
-c:a aac -b:a 192k -ar 48000 -movflags +faststart final/ad.mp4
```

**Without music.** The natural sound is kept at a modest -23 LUFS, so it doesn't hiss and there is room for music later:

```bash
ffmpeg -y -i final/raw_1080.mp4 -loop 1 -framerate 24 -t $CD -i work/card.png -filter_complex "\
[1:v]format=rgba,fade=t=in:st=0:d=0.8:alpha=1,setpts=PTS-STARTPTS+$CS/TB[card];\
[0:v]scale=$W:$H:flags=lanczos,setsar=1[base];\
[base][card]overlay=0:0:eof_action=pass:format=auto,format=yuv420p[v];\
[0:a]highpass=f=50,loudnorm=I=-23:TP=-2:LRA=11[a]" \
-map "[v]" -map "[a]" -t $D -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
-c:a aac -b:a 192k -ar 48000 -movflags +faststart final/ad.mp4
```

**Without a card:**
- drop the card input and its three video filter lines
- map `0:v` with `-c:v copy`
- the music becomes input 1, so `[2:a]` becomes `[1:a]`

LUFS is a loudness unit. -14 is the usual level for Instagram and YouTube. The models' own sound comes in quiet: about -30 for Seedance and about -25 for Kling. That is why it gets +3 dB under the music.

### 6d. Check before saying it's done

- **Size and length:** run `ffprobe` on `final/ad.mp4` and check the duration and the size.
- **Loudness:** run `ffmpeg -i final/ad.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12`. Aim for about -14 LUFS with music (-23 without) and a peak below -1 dBFS.
- **The card:** grab a frame 1.5 seconds after the card starts, and the last frame. Open both and check:
  - the text reads clearly against what is behind it
  - nothing is cut off
  - it doesn't cover the subject
  - the Hebrew is in the right order

## Step 7: deliver

1. **The file:** copy `final/ad.mp4` to `final/<brand> - פרסומת.mp4`. Give the full path, open the folder for the user, and send the file if you can.
2. **PROMPT.md:** update it with what's needed for the next ad or a variation:
   - the level, the prompt and the settings
   - both draft job IDs (a draft can still be finished within 7 days)
   - the credits spent
   - the card text
3. **The message:** tell the user in a few short Hebrew sentences:
   - what was made
   - the total credits
   - where the file is
   - what can still change: the card or the music cost nothing to redo, while new shots need a new generation

## Guardrails

- **Facts:** the card and the plan say only what the user said.
  - Don't invent prices, discounts, awards or claims.
  - No medical, financial or cosmetic promises, such as "heals", "anti-aging", "removes wrinkles" or "clinically proven". Show the feeling instead.
- **People:**
  - Everyone on screen is invented.
  - No celebrities and no look-alikes of real people.
  - No real brands or logos, except the user's own, added in the edit from their file.
- **Children:** everyday modest clothing only. Never write swimwear, bath or undressing scenes for them.
- **Real places and products:** when the ad shows one that is generated, it looks close to the real thing, not identical. Say so in the plan. Suggest a small "הדמיה" note on the card; for real estate it is standard.
- **Credits:** never spend without a clear yes, never retry without asking, and never finish a draft the user hasn't watched and chosen.

## When something goes wrong

- **Faces change between shots:** use fewer people and more distinct clothing colors, and describe each person once at the top.
- **The model ignores the shot timing:** use fewer shots and simpler actions.
- **Gibberish text** on signs, cups or screens: take those objects out of the shots, and keep the "no text" lines. Kling is the most likely to add a shop sign. Say "plain facade, no shop sign" inside the shot line, or pick the other version; a sign can't be removed later.
- **It still looks "AI":** remove hype words, add camera language (handheld, 35mm, natural light), and choose quieter everyday moments.
- **A job failed:** check its status with `jobs_wait` before doing anything. Don't resubmit blindly.

---
Made by Ofir Asher · BNA · instagram.com/ofir.ai
