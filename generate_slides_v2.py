import os
import io

slides_dir = r'C:\Users\kadackij\Documents\projects\et26_presentation\src\components\slides'
os.makedirs(slides_dir, exist_ok=True)

slides = {
    '01-Title.astro': '''---
---
<section class="slide title-slide" style="background-image: url('/images/title_bg_1791469199225.jpg');">
  <div class="title-overlay"></div>
  <div class="title-content flex-center text-center">
    <h1 class="glitch-text text-huge neon-cyan" data-text="D2C НА СТЕРОИДАХ">D2C НА СТЕРОИДАХ</h1>
    <h2 class="text-glow neon-magenta mt-8" style="font-size: 3rem;">Как 3 человека и AI-агенты<br>перестраивают e-commerce платформу FINN FLARE</h2>
    <div class="speaker-info mt-12">
      <p class="text-xl">Илья Кадацкий</p>
      <p class="text-dim">Электронная торговля 2026</p>
    </div>
  </div>
</section>
''',
    
    '02-RedesignCult.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/this_is_fine_meeting_1791469210421.jpg" alt="This is fine meeting" />
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
    <img src="/images/legacy_monster_hammer_1791469222375.jpg" alt="Legacy Monster Tech Debt" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Знакомьтесь, Лоскутик (Legacy)</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Монолитное легаси</h3>
        <p>Старые системы, обросшие костылями, патчами и невыносимым техдолгом.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Ручной привод</h3>
        <p>Мерчандайзинг через копирование в текстовые поля админки.</p>
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
    <img src="/images/ai_tornado_1791469237366.jpg" alt="AI Chaos Tornado" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">ИИ поверх хаоса: иллюзия таблетки</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Масштабирование хаоса</h3>
        <p>Внедрение ИИ поверх грязных данных и разрозненных таблиц лишь генерирует галлюцинации.</p>
      </div>
      <div class="bullet-item mt-8 border-cyan p-4">
        <h3 class="neon-cyan">Фундамент для технологий</h3>
        <p>Чтобы ИИ приносил деньги, сначала нужен порядок:</p>
        <ul class="mt-4">
          <li>Структурированный PIM</li>
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
    <img src="/images/mobile_cage_1791469255088.jpg" alt="Mobile Cage" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Мобилка «в аренде» (SaaS-ловушка)</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №1: Зависимость</h3>
        <p>Главный генератор 60% D2C-выручки упирается в чужой бэклог.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №2: Утечка ноу-хау</h3>
        <p>Любые ваши успешные фичи провайдер тиражирует конкурентам.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №3: Архитектурная шизофрения</h3>
        <p>Две разные админки, двойной ввод контента, рассинхрон остатков.</p>
      </div>
    </div>
  </div>
</section>
''',

    '06-HeadlessDeity.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/headless_deity_1791467872673.jpg" alt="Headless Deity" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Headless: Единый мозг и независимые витрины</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Единый модульный бэкенд</h3>
        <p>PIM, промо-механики, остатки, профиль клиента, чекаут.</p>
      </div>
      <div class="bullet-item mt-6">
        <h3 class="neon-magenta">Равноправные фронтенды</h3>
        <ul class="text-sm mt-2">
          <li><strong>Web:</strong> быстрая серверная генерация для SEO.</li>
          <li><strong>App:</strong> единый код на Flutter (iOS/Android).</li>
          <li><strong>МПК:</strong> рабочее место для 300 консультантов.</li>
        </ul>
      </div>
      <div class="bullet-item glow-box border-green mt-6">
        <p>Настроил один раз -> применилось везде мгновенно.</p>
      </div>
    </div>
  </div>
</section>
''',

    '07-Democratization.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/neon_vault.jpg" alt="Neon Vault Savings" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Демократизация Enterprise</h2>
    <h3 class="text-dim mt-2">Как среднему бренду делать «по-взрослому»</h3>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Смена парадигмы</h3>
        <p>Зрелые open-source решения позволяют развернуть архитектуру лидеров без космических бюджетов.</p>
      </div>
      <div class="bullet-item border-green p-4 mt-6">
        <h3 class="neon-green">Метрики трансформации:</h3>
        <ul class="mt-4">
          <li>Снижение затрат на команду в <strong>3 раза</strong>.</li>
          <li>Ускорение Time-to-Market в <strong>2-3 раза</strong>.</li>
          <li>TCO ниже, чем поддержка легаси и комиссии SaaS.</li>
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
    <img src="/images/ai_exoskeletons_1791469271500.jpg" alt="AI Exoskeletons Team" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Оргмодель «3 человека + AI»</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Отказ от длинного плеча аутсорса</h3>
        <p>Компактная in-house команда: Архитектор/CPO + 2 senior-разработчика.</p>
      </div>
      <div class="bullet-item mt-6">
        <h3 class="neon-magenta">AI-экзоскелет для разработки</h3>
        <p>Практика применения Cursor, Antigravity, Gemini:</p>
        <ul class="text-sm mt-2">
          <li>Аудит легаси за часы (вместо месяцев).</li>
          <li>Автогенерация проектной доки и БД.</li>
          <li>Ускорение разработки и прототипирования.</li>
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
    <img src="/images/cyber_slums_temple_1791469282903.jpg" alt="Cyber Slums vs Temple" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Управление переходом: Parallel Build</h2>
    
    <div class="bullet-list mt-8">
      <div class="bullet-item">
        <h3 class="neon-magenta">Feature Freeze</h3>
        <p>Мораторий на доработки старого сайта. Запрет на инвестиции в то, что пойдет под снос.</p>
      </div>
      <div class="bullet-item mt-6">
        <h3 class="neon-magenta">Parallel Build → Cutover</h3>
        <p>Старая система продает, пока рядом строится новый контур:</p>
        <ul class="mt-2 text-sm text-dim">
          <li><strong>Фаза 1:</strong> MVP (PIM + CMS + web-фронт)</li>
          <li><strong>Фаза 2:</strong> Core Commerce (бэк для Flutter)</li>
          <li><strong>Фаза 3:</strong> Scale (OMS, лояльность)</li>
        </ul>
        <p class="mt-4 text-white">Бесшовное переключение без просадки продаж.</p>
      </div>
    </div>
  </div>
</section>
''',

    '10-QA.astro': '''---
---
<section class="slide title-slide" style="background-image: url('/images/title_bg_1791469199225.jpg');">
  <div class="title-overlay"></div>
  <div class="title-content flex-center text-center">
    <h1 class="neon-magenta text-huge">D2C НА СТЕРОИДАХ</h1>
    <h2 class="mt-8 neon-cyan">Вопросы?</h2>
    
    <div class="speaker-info mt-12">
      <p class="text-xl">Илья Кадацкий</p>
      <p class="text-dim">FINN FLARE</p>
    </div>
  </div>
</section>
'''
}

for name, content in slides.items():
    with io.open(os.path.join(slides_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)

print('Slides v2 generated.')
