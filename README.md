# Diamond Pro Bar - Выездной бар в Москве

Полнофункциональный сайт выездного бара с админ-панелью Sveltia CMS, работающий на GitHub Pages.

## 🚀 Быстрый старт за 10 минут

### 1️⃣ Подготовка репозитория (2 мин)

```bash
# 1. Создайте новый репозиторий на GitHub
# https://github.com/new
# Название: diamond-pro-bar
# Описание: Выездной бар Diamond Pro Bar
# Публичный репозиторий

# 2. Клонируйте и скопируйте файлы
git clone https://github.com/yourusername/diamond-pro-bar.git
cd diamond-pro-bar

# (Скопируйте все файлы проекта в эту папку)

# 3. Установите зависимости
npm install

# 4. Отправьте на GitHub
git add .
git commit -m "Initial commit: Diamond Pro Bar website"
git push origin main
```

### 2️⃣ Включение GitHub Pages (1 мин)

1. Перейдите в **Settings** вашего репозитория
2. В левом меню выберите **Pages**
3. В "Source" выберите:
   - Branch: `main`
   - Folder: `/` (root)
4. Нажмите **Save**

Сайт будет доступен через 2-3 минуты на:
```
https://yourusername.github.io/diamond-pro-bar
```

### 3️⃣ Настройка GitHub OAuth для админ-панели (3 мин)

#### Шаг 1: Создайте OAuth приложение

1. Перейдите в **Settings** → **Developer settings** → **OAuth Apps**
2. Нажмите **New OAuth App**
3. Заполните:
   - **Application name**: `Diamond Pro Bar CMS`
   - **Homepage URL**: `https://yourusername.github.io/diamond-pro-bar`
   - **Authorization callback URL**: `https://yourusername.github.io/diamond-pro-bar/admin`
4. Нажмите **Register application**
5. Скопируйте **Client ID** и нажмите "Generate new client secret"

#### Шаг 2: Получите доступ через Sveltia

Используйте приватный режим браузера и перейдите на:
```
https://yourusername.github.io/diamond-pro-bar/admin
```

При первом входе:
- Авторизуйтесь на GitHub с OAuth
- Sveltia сохранит ваш токен локально

### 4️⃣ Обновите конфигурацию (2 мин)

#### Обновите `admin/config.yml`:
```yml
backend:
  name: github
  repo: yourusername/diamond-pro-bar  # ← Измените на ваш репо
  branch: main

media_folder: public/images/uploads
public_folder: /diamond-pro-bar/images/uploads  # ← Если URL другой, измените base
```

#### Обновите `astro.config.mjs`:
```javascript
export default defineConfig({
  site: 'https://yourusername.github.io',  // ← Ваш GitHub Pages URL
  base: '/diamond-pro-bar',                   // ← Имя репозитория
});
```

### 5️⃣ Обновите контактные данные (2 мин)

В `src/data/global.json` и `src/data/contacts.json` замените:
- ✏️ Номер телефона: `+7 (999) 999-99-99`
- ✏️ WhatsApp: `+7 (999) 999-99-99`
- ✏️ Email: `info@diamondprobar.ru`
- ✏️ Социальные сети: Instagram, VK, Telegram, TikTok

```bash
# Отправьте изменения
git add .
git commit -m "Update contact information"
git push origin main
```

**Готово! 🎉**

---

## 📝 Работа с админ-панелью

### Доступ к админ-панели:
```
https://yourusername.github.io/diamond-pro-bar/admin
```

### Что можно редактировать:

1. **Глобальные настройки** (Global Settings)
   - Названиесайта, логотип
   - Контактные данные
   - Социальные сети

2. **Услуги / Пакеты** (Services)
   - Добавляйте новые пакеты баров
   - Редактируйте цены
   - Загружайте фото

3. **Меню** (Menu)
   - Коктейли, кофе, смузи
   - Ингредиенты и цены
   - Категоризация

4. **Кейсы** (Cases / Portfolio)
   - Примеры реализованных событий
   - Фото и описания

5. **Блог** (Blog)
   - Написание статей в Markdown
   - Публикация новостей

6. **Контакты** (Contacts)
   - Телефон, email, WhatsApp
   - Часы работы
   - Адрес

7. **FAQ**
   - Часто задаваемые вопросы

8. **Отзывы** (Testimonials)
   - Добавляйте отзывы клиентов

### Как опубликовать контент:

1. Откройте админ-панель
2. Перейдите в нужную коллекцию (например, "Services")
3. Нажмите "+ New" (или "+" кнопка)
4. Заполните поля
5. **Важно**: Нажмите **"Publish"** внизу формы
6. GitHub Actions автоматически соберет сайт (2-5 минут)
7. Сайт обновится автоматически

---

## 📱 Структура страниц

```
/diamond-pro-bar/
├── /                   👈 Главная (услуги, как это работает)
├── /menu/             👈 Меню коктейлей, кофе, смузи
├── /services/         👈 Подробно об услугах и калькулятор
├── /cases/            👈 Портфолио и отзывы
├── /blog/             👈 Блог со статьями
├── /contact/          👈 Контакты и форма заявки
└── /admin             👈 Админ-панель (CMS)
```

---

## 🎨 Персонализация

### Измените цвета в `tailwind.config.mjs`:

```javascript
colors: {
  gold: '#D4AF37',           // Основной цвет
  'dark-bg': '#0A0E27',      // Фон
  neon: '#00FF88',           // Неоновый зеленый
  'neon-pink': '#FF006E',    // Неоновый розовый
}
```

### Измените шрифты:

В `src/layouts/Layout.astro` измените Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=YOUR_FONT:wght@700&display=swap" rel="stylesheet" />
```

### Добавьте свой логотип:

1. Поместите логотип в `public/logo.svg` или `public/logo.png`
2. Обновите в `src/components/Header.astro` путь до логотипа

---

## 📞 Контактные интеграции

### WhatsApp кнопки:

Все кнопки "Написать в WhatsApp" отправляют на:
```
https://wa.me/79999999999
```

Измените номер на ваш в:
- `src/components/Header.astro`
- `src/components/Hero.astro`
- `src/pages/*.astro`

**Замените `79999999999` на ваш номер без пробелов**

### Форма заявки:

Форма на странице `/contact/` автоматически:
1. Собирает данные
2. Отправляет в WhatsApp с полным текстом заявки

Интеграция через `https://wa.me/` - не требует дополнительной настройки.

---

## 🔧 Локальная разработка

### Запустите сайт локально:

```bash
npm install
npm run dev
```

Откройте браузер: `http://localhost:3000/diamond-pro-bar`

### Сборка для production:

```bash
npm run build
npm run preview
```

---

## 🐛 Решение проблем

### "GitHub Pages еще не активна"
- **Решение**: Подождите 2-3 минуты после первого push
- Проверьте Settings → Pages → Source

### "Админ-панель не загружается"
- **Решение**: Очистите кэш браузера (Ctrl+Shift+Delete)
- Используйте приватный режим браузера

### "Фото не загружаются"
- **Решение**: Используйте JPEG или PNG максимум 5MB
- Проверьте, чтобы папка `public/images/uploads/` существовала

### "Изменения не отражаются на сайте"
- **Решение**: GitHub Actions может работать 2-5 минут
- Проверьте статус: Actions → Последний workflow
- Если ошибка - прочитайте лог

### "OAuth не работает"
- **Убедитесь**:
  1. Репозиторий публичный
  2. OAuth App настроена с правильными URL
  3. Используется приватный режим браузера

---

## 📊 SEO и метаданные

Сайт оптимизирован для SEO:
- Open Graph мета-теги
- Twitter Card
- Canonical URLs
- Структурированные данные

Для каждой страницы может быть описание в админ-панели.

---

## 📈 Аналитика

Добавьте Google Analytics в `src/layouts/Layout.astro`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 🚀 Деплой готов!

**GitHub Actions автоматически:**
- ✅ Собирает сайт при каждом push
- ✅ Публикует на GitHub Pages
- ✅ Обновляет содержимое из админ-панели

**Всё работает без дополнительных действий!**

---

## 📚 Дополнительные ресурсы

- [Astro документация](https://docs.astro.build)
- [Tailwind CSS](https://tailwindcss.com)
- [Sveltia CMS документация](https://github.com/sveltia/cms)
- [GitHub Pages документация](https://docs.github.com/en/pages)

---

## 📄 Лицензия

MIT

---

**Diamond Pro Bar © 2024**
Выездной бар под ключ в Москве и МО
