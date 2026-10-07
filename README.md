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
