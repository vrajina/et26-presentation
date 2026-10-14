import os
import io

slides_dir = r'C:\Users\kadackij\Documents\projects\et26_presentation\src\components\slides'
os.makedirs(slides_dir, exist_ok=True)

slides = {
    '01-Title.astro': '''---
---
<section class="slide title-slide" style="background-image: url('/images/deus_title.jpg');">
  <div class="title-overlay"></div>
  <div class="title-content flex-center text-center">
    <h1 class="glitch-text text-huge neon-cyan" style="font-size: 5rem; margin-bottom: 1rem;">D2C на стероидах</h1>
    <h2 class="text-glow neon-magenta mt-8" style="font-size: 2.5rem;">Как 3 человека и AI-агенты<br>перестраивают e-commerce платформу FINN FLARE</h2>
  </div>
  <div class="speaker-info-bottom">
    <p class="text-xl" style="font-size: 2.2rem; color: #d4af37;">Илья Кадацкий</p>
    <p class="text-dim" style="font-size: 1.6rem;">Электронная торговля 2026</p>
  </div>
</section>
''',
    
    '02-RedesignCult.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_this_is_fine.jpg" alt="This is fine meeting" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Культ редизайнов при горящем бэкенде</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Косметический ремонт не лечит</h3>
        <p>Ритейл годами инвестирует в полировку фронтенда, пока под капотом — пожар.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Цена «красоты»</h3>
        <p>Падение скорости загрузки, каскадные баги и невозможность гибко менять каталог.</p>
      </div>
      <div class="bullet-item glow-box border-magenta mt-8">
        <h3 class="neon-cyan">Вывод:</h3>
        <p>Чтобы масштабировать продажи, нужно перестать полировать фасад и пересобрать коммерческое ядро.</p>
      </div>
    </div>
  </div>
</section>
''',

    '03-LegacyPatchwerk.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_legacy_monster.jpg" alt="Legacy Monster Tech Debt" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Знакомьтесь, Лоскутик (legacy)</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Монолитное легаси</h3>
        <p>Старые системы, обросшие костылями, патчами и невыносимым техдолгом.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Ручной привод</h3>
        <p>Мерчандайзинг через ручное копирование данных в текстовые поля админки.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Хрупкость</h3>
        <p>Любое изменение может «уронить» весь магазин. Монстр еле двигается.</p>
      </div>
    </div>
  </div>
</section>
''',

    '04-AIChaos.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_ai_tornado.jpg" alt="AI Chaos Tornado" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">ИИ поверх хаоса: иллюзия таблетки</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Масштабирование хаоса</h3>
        <p>Внедрение ИИ поверх грязных данных и разрозненных таблиц лишь успешно масштабирует этот хаос и генерирует галлюцинации.</p>
      </div>
      <div class="bullet-item mt-8 border-cyan p-4">
        <h3 class="neon-cyan">Фундамент для технологий</h3>
        <p>Чтобы ИИ приносил деньги, сначала нужен порядок:</p>
        <ul class="mt-4">
          <li>Структурированный PIM-каталог</li>
          <li>Единый профиль клиента</li>
          <li>Честный учет остатков</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '05-MobileTrap.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_holy_grail.jpg" alt="Mobile Holy Grail" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Приложение «в аренде» — ловушка SaaS</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №1: Зависимость</h3>
        <p>Мобильное приложение дает до 60% D2C-выручки, но его развитие полностью упирается в чужой бэклог.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №2: Утечка ноу-хау</h3>
        <p>Любые ваши успешные фичи провайдер немедленно тиражирует конкурентам.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №3: Архитектурная шизофрения</h3>
        <p>Две разные админки, двойной ввод контента, рассинхронизация остатков.</p>
      </div>
    </div>
  </div>
</section>
''',

    '06-HeadlessDeity.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_headless_shiva.jpg" alt="Headless Deity" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Headless: единый мозг и независимые витрины</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Единый модульный бэкенд</h3>
        <p>PIM, промо-механики, остатки, профиль клиента, чекаут — всё управляется из одной точки.</p>
      </div>
      <div class="bullet-item mt-6">
        <h3 class="neon-magenta">Равноправные фронтенды</h3>
        <ul class="text-sm mt-4">
          <li><strong>Web:</strong> быстрая серверная генерация для SEO.</li>
          <li><strong>App:</strong> единый код на Flutter (iOS и Android).</li>
          <li><strong>МПК:</strong> рабочее место для 300 консультантов розницы.</li>
        </ul>
      </div>
      <div class="bullet-item glow-box border-green mt-6">
        <p>Настроил один раз — применилось везде мгновенно.</p>
      </div>
    </div>
  </div>
</section>
''',

    '07-Democratization.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_democratization.jpg" alt="Democratization Workshop" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Демократизация enterprise</h2>
    <h3 class="text-dim mt-2">Как среднему бренду делать «по-взрослому»</h3>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Смена парадигмы</h3>
        <p>Зрелые open-source решения позволяют небольшой команде развернуть архитектуру лидеров без космических бюджетов.</p>
      </div>
      <div class="bullet-item border-green p-4 mt-6">
        <h3 class="neon-green">Метрики трансформации:</h3>
        <ul class="mt-4">
          <li>Снижение затрат на команду в <strong>3 раза</strong>.</li>
          <li>Ускорение Time-to-Market в <strong>2—3 раза</strong>.</li>
          <li>Общая стоимость владения (TCO) ниже, чем поддержка легаси и комиссии SaaS.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '08-OrgModel.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_warhammer.jpg" alt="Warhammer Developers" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Оргмодель «3 человека + AI»</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Отказ от длинного плеча аутсорса</h3>
        <p>Компактный in-house спецназ: архитектор-CPO и два senior-разработчика работают напрямую с бизнесом.</p>
      </div>
      <div class="bullet-item mt-6">
        <h3 class="neon-magenta">Экзоскелеты для разработки</h3>
        <p>Практика боевого применения Cursor, Antigravity и Gemini:</p>
        <ul class="text-sm mt-4">
          <li>Аудит легаси-кода за часы, а не месяцы.</li>
          <li>Автогенерация проектной документации и структуры БД.</li>
          <li>Многократное ускорение разработки и прототипирования.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '09-Cutover.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/cyber_slums.jpg" alt="Cyber Slums vs Temple" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Управление переходом: parallel build</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Feature freeze</h3>
        <p>Жесткий мораторий на доработки старого сайта. Запрет на инвестиции в то, что скоро пойдет под снос.</p>
      </div>
      <div class="bullet-item mt-6">
        <h3 class="neon-magenta">Параллельная стройка</h3>
        <p>Старая система продает, пока рядом строится новый контур:</p>
        <ul class="mt-4 text-sm text-dim">
          <li><strong>Фаза 1:</strong> MVP (PIM, CMS, web-фронт)</li>
          <li><strong>Фаза 2:</strong> Core Commerce (бэкенд для Flutter)</li>
          <li><strong>Фаза 3:</strong> Scale (OMS, система лояльности)</li>
        </ul>
        <p class="mt-4 text-white">Бесшовный cutover без просадки продаж и SEO-трафика.</p>
      </div>
    </div>
  </div>
</section>
''',

    '10-QA.astro': '''---
---
<section class="slide title-slide" style="background-image: url('/images/deus_final_dawn.jpg');">
  <div class="title-overlay" style="background: rgba(10, 10, 12, 0.4);"></div>
  <div class="title-content flex-center text-center">
    <h1 class="neon-magenta text-huge" style="margin-bottom: 2rem;">Второе дыхание бизнеса</h1>
    <h2 class="neon-cyan">Вопросы?</h2>
  </div>
  <div class="speaker-info-bottom">
    <p class="text-xl" style="color: #d4af37;">Илья Кадацкий</p>
    <p class="text-dim">FINN FLARE</p>
  </div>
</section>
'''
}

for name, content in slides.items():
    with io.open(os.path.join(slides_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)

print('Slides v3 generated.')
