# Medication names

Apply this rule across all note types and output modes.

- If a medication is supplied as a brand/trade/product name, retain its exact documented name and immediately append the verified generic (active-ingredient) name in ordinary parentheses: `Brand (generic)`. Apply this to every occurrence so separately copied fields remain understandable.
- Use the generic identity supplied in the source when unambiguous and consistent. Otherwise verify the exact product using an authoritative regulator label, official manufacturer label, or applicable institutional formulary. For Taiwanese products, prefer TFDA-approved product information or the applicable hospital formulary. Do not rely on spelling similarity, a guessed correction, or an unverified remembered mapping.
- Reference lookups may contain only product-identification details needed to resolve the medicine, such as name, manufacturer, market, strength, or dosage form. Never send patient names, identifiers, symptoms, diagnoses, dates of care, record excerpts, or other clinical context to a search engine or external service. This narrow product-only lookup is the sole exception to the note skills' external-source prohibition.
- Match the actual market, formulation, and documented product. Include all active ingredients for a combination medicine, separated by ` / `. Retain a salt or formulation distinction when clinically material. Do not infer a missing strength, dose, route, frequency, duration, indication, or treatment change from a product label.
- If identity remains ambiguous, conflicting, misspelled, or unverifiable, preserve the supplied brand alone and flag the specific identity for confirmation in `Physician considerations — outside the medical record`. Do not append a guessed generic or an in-record `unknown` placeholder. For holistic care, use its existing required-domain gap mechanism rather than duplicate outside-record considerations.
- If the input already says `Brand (generic)`, verify consistency without adding another pair. A generic-only input remains generic-only; never invent a brand. Preserve the original name, dose, units, route, frequency, duration, hold criteria, timing, allergy reaction, and action status.
- Keep verification citations and uncertainty outside the copy-ready record when they must be shown; no search commentary belongs inside it.

Before finalizing, check every included medication occurrence for a supplied brand, verified ingredient identity, no duplicate annotation, all combination ingredients, and unchanged prescription details.
