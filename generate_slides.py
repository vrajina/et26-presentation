import os
import io

slides_dir = r'C:\Users\kadackij\Documents\projects\et26_presentation\src\components\slides'
os.makedirs(slides_dir, exist_ok=True)

slides = {
    '01-Title.astro': '''---
---
<section class="slide slide-cover">
  <div class="content flex-center text-center">
    <h1 class="glitch-text text-huge neon-cyan" data-text="D2C НА СТЕРОИДАХ">D2C НА СТЕРОИДАХ</h1>
    <h2 class="text-glow neon-magenta mt-8">Как 3 человека и AI-агенты<br>перестраивают e-commerce платформу FINN FLARE</h2>
    
    <div class="speaker-info mt-12">
      <p class="text-xl">Илья Кадацкий</p>
      <p class="text-dim">Электронная торговля 2026</p>
    </div>
  </div>
</section>
''',
    
    '02-RedesignCult.astro': '''---
---
<section class="slide layout-split">
  <div class="content">
    <h2 class="neon-cyan">Культ редизайнов при горящем бэкенде</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3>Косметический ремонт не лечит</h3>
        <p>Ритейл годами инвестирует в полировку фронтенда и перерисовку карточек, пока под капотом — пожар.</p>
      </div>
      <div class="bullet-item">
        <h3>Цена «красоты»</h3>
        <p>Падение скорости загрузки, каскадные баги при доработках и невозможность гибко менять каталог под сезонность.</p>
      </div>
      <div class="bullet-item glow-box border-magenta mt-8">
        <h3 class="neon-magenta">Вывод:</h3>
        <p>Чтобы масштабировать продажи, нужно перестать полировать фасад и пересобрать коммерческое ядро.</p>
      </div>
    </div>
  </div>
  <div class="visual flex-center bg-dark">
    <!-- Abstract representation of a polished facade hiding fire -->
    <div class="text-center">
      <h1 class="neon-magenta" style="font-size: 6rem; opacity: 0.5;">UI</h1>
      <p class="text-dim">?????? Backend is on fire ??????</p>
    </div>
  </div>
</section>
''',

    '03-LegacyPatchwerk.astro': '''---
---
<section class="slide layout-split">
  <div class="content">
    <h2 class="neon-cyan">Знакомьтесь, Лоскутик (Legacy)</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3>Монолитное легаси</h3>
        <p>Старые системы (например, 1С-Битрикс без обновлений), обросшие костылями и патчами.</p>
      </div>
      <div class="bullet-item">
        <h3>Ручной привод</h3>
        <p>Мерчандайзинг через Figma и ручное копирование в текстовые поля админки.</p>
      </div>
      <div class="bullet-item">
        <h3>Хрупкость</h3>
        <p>Любое изменение может «уронить» весь магазин. Монстр еле двигается.</p>
      </div>
    </div>
  </div>
  <div class="visual image-full">
    <img src="/images/legacy_monster_1791467854596.jpg" alt="Legacy Monster" />
  </div>
</section>
''',

    '04-AIChaos.astro': '''---
---
<section class="slide">
  <div class="content">
    <h2 class="neon-cyan text-center">ИИ поверх хаоса: почему нельзя автоматизировать беспорядок</h2>
    
    <div class="grid-2 mt-12 gap-8">
      <div class="card border-magenta">
        <h3 class="neon-magenta">Иллюзия волшебной таблетки</h3>
        <p class="mt-4">Ритейл пытается внедрять ИИ в персонализацию, поиск и мерчандайзинг поверх грязных данных, разрозненных таблиц и ручных выгрузок.</p>
        <p class="mt-4 text-dim">Результат: ИИ лишь масштабирует хаос и генерирует галлюцинации.</p>
      </div>
      <div class="card border-cyan">
        <h3 class="neon-cyan">Фундамент для технологий</h3>
        <p class="mt-4">Чтобы ИИ приносил деньги, сначала нужен порядок на бэкенде:</p>
        <ul class="mt-4 tech-list">
          <li>Структурированный каталог (PIM)</li>
          <li>Единый профиль клиента</li>
          <li>Честный омниканальный учет остатков</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '05-MobileTrap.astro': '''---
---
<section class="slide layout-split">
  <div class="content">
    <h2 class="neon-cyan">Мобилка дает 60% продаж, но живет «в аренде»</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3>Скрытые угрозы SaaS-витрин</h3>
        <p>Главный генератор D2C-выручки упирается в чужой бэклог.</p>
      </div>
      <div class="bullet-item border-magenta p-4 mt-4">
        <h4 class="neon-magenta">Риск №1: Зависимость</h4>
        <p class="text-sm">Развитие зависит от провайдера.</p>
      </div>
      <div class="bullet-item border-magenta p-4 mt-4">
        <h4 class="neon-magenta">Риск №2: Утечка ноу-хау</h4>
        <p class="text-sm">Любые ваши успешные фичи тиражируются на конкурентов.</p>
      </div>
      <div class="bullet-item border-magenta p-4 mt-4">
        <h4 class="neon-magenta">Риск №3: Архитектурная шизофрения</h4>
        <p class="text-sm">Две разные админки, двойной ввод контента, рассинхрон остатков.</p>
      </div>
    </div>
  </div>
  <div class="visual flex-center bg-dark text-center border-left-cyan">
    <h3 class="neon-cyan text-4xl leading-tight">Стратегический выбор:<br>Собственная мобильная платформа<br>на едином бэкенде.</h3>
  </div>
</section>
''',

    '06-HeadlessDeity.astro': '''---
---
<section class="slide layout-split reverse">
  <div class="content">
    <h2 class="neon-cyan">Headless: Единый мозг и независимые витрины</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-cyan">Единый модульный бэкенд</h3>
        <p>PIM, промо-механики, остатки, профиль клиента, чекаут.</p>
      </div>
      <div class="bullet-item mt-6">
        <h3 class="neon-magenta">Равноправные фронтенды</h3>
        <ul class="text-sm mt-2">
          <li><strong>Web-витрина:</strong> быстрая генерация для SEO.</li>
          <li><strong>Кастомное приложение:</strong> единый код на Flutter (iOS/Android).</li>
          <li><strong>МПК:</strong> рабочее место для 300 консультантов розницы.</li>
        </ul>
      </div>
      <div class="bullet-item glow-box border-green mt-6">
        <h3 class="neon-green">Единое окно управления</h3>
        <p class="text-sm">Настроил один раз -> применилось везде мгновенно.</p>
      </div>
    </div>
  </div>
  <div class="visual image-full">
    <img src="/images/headless_deity_1791467872673.jpg" alt="Headless Deity" />
  </div>
</section>
''',

    '07-Democratization.astro': '''---
---
<section class="slide">
  <div class="content text-center">
    <h2 class="neon-cyan">Демократизация Enterprise</h2>
    <h3 class="text-dim mt-2">Как среднему бренду делать «по-взрослому» без космических бюджетов</h3>
    
    <div class="grid-2 mt-12 gap-8 text-left">
      <div class="card">
        <h3 class="neon-magenta">Смена парадигмы</h3>
        <p class="mt-4">Зрелые open-source решения позволяют развернуть архитектуру лидеров рынка. Больше не нужны десятки миллионов и годы разработки.</p>
      </div>
      <div class="card border-green">
        <h3 class="neon-green text-3xl">Метрики трансформации</h3>
        <ul class="mt-6 big-list">
          <li>Снижение затрат на команду в <strong>3 раза</strong></li>
          <li>Ускорение Time-to-Market в <strong>2-3 раза</strong></li>
          <li>TCO своей платформы ниже, чем поддержка легаси и комиссии SaaS.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '08-OrgModel.astro': '''---
---
<section class="slide layout-split">
  <div class="content">
    <h2 class="neon-cyan">Оргмодель «3 человека + AI»</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3>Отказ от длинного плеча аутсорса</h3>
        <p>Исключение цепочек: аккаунт > PM > аналитик > тимлид > джун.</p>
      </div>
      <div class="bullet-item mt-4">
        <h3 class="neon-magenta">In-house спецназ</h3>
        <p>Архитектор/CPO + 2 senior-разработчика напрямую с бизнесом.</p>
      </div>
      <div class="bullet-item mt-4">
        <h3 class="neon-green">Практика AI-агентов (Cursor, Antigravity, Gemini)</h3>
        <ul class="text-sm mt-2">
          <li>Аудит легаси за часы (а не месяцы).</li>
          <li>Автогенерация проектной доки и БД.</li>
          <li>Быстрое прототипирование админки.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="visual image-full">
    <img src="/images/cyber_team_potions_1791467890393.jpg" alt="Cyber AI Team" />
  </div>
</section>
''',

    '09-Cutover.astro': '''---
---
<section class="slide">
  <div class="content">
    <h2 class="neon-cyan text-center">Управление переходом: Parallel Build > Cutover</h2>
    
    <div class="timeline mt-12">
      <div class="timeline-item border-magenta">
        <div class="timeline-dot bg-magenta"></div>
        <h3>Feature Freeze</h3>
        <p>Мораторий на доработки старого сайта. Запрет на инвестиции в то, что пойдет под снос.</p>
      </div>
      <div class="timeline-item border-cyan">
        <div class="timeline-dot bg-cyan"></div>
        <h3>Parallel Build</h3>
        <p>Старая система продает, пока рядом строится новый контур:</p>
        <ul class="mt-2 text-sm text-dim">
          <li>Фаза 1: MVP (PIM + CMS + web-фронт)</li>
          <li>Фаза 2: Core Commerce (корзина, чекаут, бэк для Flutter)</li>
          <li>Фаза 3: Scale (OMS, лояльность, ценообразование)</li>
        </ul>
      </div>
      <div class="timeline-item border-green">
        <div class="timeline-dot bg-green"></div>
        <h3>Cutover</h3>
        <p>Бесшовное переключение без просадки SEO-трафика и кассовых разрывов.</p>
      </div>
    </div>
  </div>
</section>
''',

    '10-QA.astro': '''---
---
<section class="slide slide-cover">
  <div class="content flex-center text-center">
    <h1 class="neon-magenta text-huge">FIGHT!</h1>
    <h2 class="mt-8 neon-cyan">Вопросы?</h2>
    
    <div class="speaker-info mt-12">
      <p class="text-xl">Илья Кадацкий</p>
      <p class="text-dim">FINN FLARE</p>
      <p class="mt-4 text-sm">tg: @kadackij</p>
    </div>
  </div>
</section>
'''
}

for name, content in slides.items():
    with io.open(os.path.join(slides_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)

print('Slides generated.')
