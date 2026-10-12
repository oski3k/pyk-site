# pyk-site

Publiczne strony aplikacji Pyk (GitHub Pages): polityka prywatności i instrukcja usuwania konta.
Linkują do nich Google Play i App Store. Kod aplikacji jest w prywatnym repo `oski3k/Pyk`.

- https://oski3k.github.io/pyk-site/privacy.html
- https://oski3k.github.io/pyk-site/delete-account.html
- https://oski3k.github.io/pyk-site/admin/ — panel ogłoszeń (logowanie i uprawnienia w Supabase).

## Aktualizacja panelu

Źródła panelu są w prywatnym repo aplikacji, w `admin/`. W tym katalogu uruchom
`npm ci` i `npm run stage:pages` (domyślnie oczekuje sąsiedniego checkoutu `pyk-site`).
Następnie sprawdź i commituj zmiany w `pyk-site/admin/`, po czym wykonaj `git push`.
GitHub Pages publikuje statyczny build; komputer nie musi być uruchomiony.
Do repo trafia tylko build z publicznym kluczem Supabase, nigdy `.env`, klucz
`service_role` ani sekrety powiadomień. Nie edytuj plików builda ręcznie.

## Strony publiczne

Strona główna jest domyślnie angielska (`index.html`), polska wersja jest
w `index-pl.html`. Zachowano adresy sklepowe `privacy.html` i
`delete-account.html` dla treści po polsku. Ich angielskie odpowiedniki to
`privacy-en.html` i `delete-account-en.html`. Wybór EN/PL prowadzi do tej samej
podstrony w drugim języku i działa bez JavaScript. Polityka zawiera także
portugalski skrót praw i informacji o transferach dla graczy z Brazylii.

Treść i wspólny szablon są w `tools/build.py`; po edycji uruchom:

```bash
python3 tools/build.py
python3 tools/check.py
git diff --check
python3 -m http.server 8765 --bind 127.0.0.1
```

Sprawdź strony przy szerokości 320 px, 390 px i na komputerze. Treść prawna
jest statycznym HTML, z bocznym spisem treści, przewijaną tabelą i układem do
druku. Wszystkie fonty i grafiki są lokalne; font aplikacji Bricolage Grotesque
ma licencję SIL OFL w `assets/fonts/OFL.txt`. Publiczne strony nie mają
analityki, cookies ani zapisu preferencji. Panel `/admin/` ma osobną sesję
Supabase i pozostaje budowany ze źródeł aplikacji zgodnie z opisem wyżej.

Design używa palety i stylu „Naklejka” z aplikacji. Ilustracja kart na stronie
głównej jest ilustracją, nie zrzutem interfejsu. Przycisk Google Play ma
adres produkcyjny `com.oskarsledz.pyk`; dostępność zależy od publikacji sklepu.

## Utrzymanie polityki

Aktualizacja 12.10.2026 obejmuje obecny kod: zdjęcia, zakupy, powiadomienia,
analitykę Supabase i Firebase, Web3Forms, blokady/zgłoszenia i funkcje opcjonalne
(wyzwanie dnia, kolejka i bilans). Region Supabase EU West/Irlandia został
potwierdzony przez właściciela. Nie deklarujemy, że usunięcie konta kasuje
Firebase, gwarantuje sukces usunięcia RevenueCat lub anuluje subskrypcję.

Audyt i konkretne kwestie pozostałe do domknięcia są w prywatnym repo
aplikacji: `docs/PUBLIC_SITE_PRIVACY_AUDIT.md`. Tekst strony nie stanowi
potwierdzenia zgodności we wszystkich jurysdykcjach. Trzeba potwierdzić
konfigurację retencji usług, podstawy/zgody na analitykę, adres administratora,
mechanizmy transferów i wymagania lokalizacyjne dla właściwych rynków.
