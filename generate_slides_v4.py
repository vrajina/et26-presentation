import os
import io

slides_dir = r"C:\Users\kadackij\Documents\projects\et26_presentation\src\components\slides"

# Remove existing slide files
for f in os.listdir(slides_dir):
    if f.endswith('.astro'):
        os.remove(os.path.join(slides_dir, f))

slides = {
    '01-Title.astro': '''---
---
<section class="slide title-slide" style="background-image: url('/images/deus_title.jpg');">
  <div class="title-overlay"></div>
  <div class="title-content flex-center text-center">
    <h1 class="glitch-text" style="font-size: 3.4rem; margin-bottom: 0.8rem; color: var(--pip-green);">D2C на&nbsp;стероидах</h1>
    <h2 style="font-size: 1.85rem; line-height: 1.35; color: var(--sega-blue); margin-bottom: 0;">Как 3&nbsp;человека и&nbsp;AI-агенты перестраивают e-commerce платформу FINN&nbsp;FLARE</h2>
  </div>
  <div class="speaker-info-bottom">
    <span class="speaker-name">Илья Кадацкий</span>
    <span class="speaker-divider">|</span>
    <span class="speaker-event">Электронная торговля’26</span>
  </div>
</section>
''',

    '02-AboutCompany.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_finnflare.jpg" alt="FINN FLARE Flagship Concept" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">О&nbsp;компании FINN&nbsp;FLARE</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Фэшн-бренд с&nbsp;60-летней историей</h3>
        <p>Скандинавская эстетика, философия комфорта, бескомпромиссная надежность и&nbsp;функциональность.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Масштабная розничная сеть</h3>
        <p>Более 40&nbsp;собственных флагманских магазинов в&nbsp;ключевых городах России.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Омниканальный цифровой контур</h3>
        <p>Собственный интернет-магазин, мобильное приложение и&nbsp;цифровые рабочие места (МПК) для&nbsp;300+ консультантов в&nbsp;рознице.</p>
      </div>
    </div>
  </div>
</section>
''',

    '03-AboutSpeaker.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_speaker_portrait.jpg" alt="Илья Кадацкий - Chief Product Architect" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Обо&nbsp;мне: Илья Кадацкий</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">20&nbsp;лет в&nbsp;диджитале и&nbsp;e-com</h3>
        <p>Архитектура, продуктовая разработка и&nbsp;масштабирование коммерческих платформ в&nbsp;ритейле.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Опыт трансформаций</h3>
        <p>Запуск и&nbsp;перезапуск цифровых каналов для&nbsp;Thomas&nbsp;Münz, MODI, Calypso, развитие D2C-направления «НАШЕ&nbsp;ЗОЛОТО».</p>
      </div>
      <div class="bullet-item glow-box border-green mt-4">
        <h3 class="neon-green" style="font-size: 1.6rem;">Миссия в&nbsp;FINN&nbsp;FLARE:</h3>
        <p>С&nbsp;весны 2025&nbsp;года — полная перестройка e-com инфраструктуры с&nbsp;нуля силами компактной команды инженеров и&nbsp;AI-агентов.</p>
      </div>
    </div>
  </div>
</section>
''',

    '04-Disposition.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_disposition.jpg" alt="Monolithic Infrastructure & 1C Disposition" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Где мы сейчас: диспозиция</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Точка&nbsp;А: барьеры монолита</h3>
        <ul style="margin-bottom: 0.8rem;">
          <li>Запутанная инфраструктура на&nbsp;базе монолитного Битрикса в&nbsp;собственном e-com</li>
          <li>Во&nbsp;всех системах и&nbsp;контурах 1С — критический объем легаси и&nbsp;техдолга</li>
          <li>Технический фактор стал главным сдерживающим барьером для&nbsp;роста продаж</li>
        </ul>
      </div>
      
      <div class="bullet-item glow-box border-cyan">
        <h3 class="neon-cyan" style="font-size: 1.6rem; margin-bottom: 0.4rem;">Что уже сделано:</h3>
        <ul style="margin-bottom: 0;">
          <li>Оптимизирована внутренняя техническая команда</li>
          <li>Снижены затраты на&nbsp;внешних подрядчиков и&nbsp;сторонние сервисы</li>
          <li>Запущен проект фундаментальной перестройки силами малой команды + AI</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '05-RedesignCult.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_this_is_fine.jpg" alt="Fashion redesign meeting during backend fire" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Фэшн и&nbsp;культ редизайна при&nbsp;горящем бэке</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Косметический ремонт не&nbsp;лечит</h3>
        <p>Фэшн-ритейл годами инвестирует бюджеты в&nbsp;полировку пикселей на&nbsp;витрине, пока под&nbsp;капотом бушует пожар архитектурного хаоса.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Реальная цена «красоты»</h3>
        <p>Катастрофическая деградация скорости отклика, каскадные баги при&nbsp;чекауте и&nbsp;невозможность быстро адаптировать каталог под&nbsp;маркетинг.</p>
      </div>
      <div class="bullet-item glow-box border-magenta">
        <h3 class="neon-cyan" style="font-size: 1.6rem; margin-bottom: 0.4rem;">Вывод:</h3>
        <p>Чтобы масштабировать продажи, нужно перестать красить фасад аварийного здания и&nbsp;заново отстроить коммерческое ядро.</p>
      </div>
    </div>
  </div>
</section>
''',

    '06-LegacyPatchwerk.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_legacy_monster.jpg" alt="Legacy Monster with Tech Debt Hammer" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Знакомьтесь, наш легаси</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Монолитный монстр на&nbsp;сайте</h3>
        <p>Десятилетний Битрикс, сшитый из&nbsp;сотен сторонних модулей, костылей и&nbsp;неподдерживаемых патчей. Неповоротлив и&nbsp;хрупок.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">В&nbsp;1С история не&nbsp;лучше</h3>
        <p>Учетные контуры ERP перегружены историческими наслоениями логики; мерчандайзинг и&nbsp;описания вручную копируются в&nbsp;админку.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Хрупкость интеграционных связок</h3>
        <p>Малейшее изменение в&nbsp;коде рискует обрушить синхронизацию остатков, чекаут или обработку онлайн-заказов.</p>
      </div>
    </div>
  </div>
</section>
''',

    '07-AIChaos.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_ai_tornado.jpg" alt="AI Data Tornado over Slums" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">ИИ поверх хаоса: иллюзия таблетки</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Автоматизация разрухи</h3>
        <p>Внедрение ИИ-инструментов поверх грязных данных и&nbsp;неструктурированных таблиц не&nbsp;решает проблем, а&nbsp;лишь стремительно масштабирует хаос и&nbsp;галлюцинации.</p>
      </div>
      
      <div class="bullet-item glow-box border-cyan">
        <h3 class="neon-cyan" style="font-size: 1.6rem; margin-bottom: 0.5rem;">Базовый фундамент для&nbsp;технологий:</h3>
        <p style="font-size: 1.35rem; margin-bottom: 0.6rem;">Чтобы ИИ генерировал чистую прибыль, сначала требуется навести строгий порядок в&nbsp;данных:</p>
        <ul style="margin-bottom: 0;">
          <li>Единый структурированный PIM-каталог товаров</li>
          <li>Сквозной цифровой профиль покупателя (CDP)</li>
          <li>Честный и&nbsp;мгновенный учет остатков по&nbsp;всей сети</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '08-MobileTrap.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_holy_grail.jpg" alt="Mobile App Holy Grail" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Приложение «в&nbsp;аренде»&nbsp;— ловушка SaaS</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №1: Критическая зависимость</h3>
        <p>Мобильное приложение дает бренду до&nbsp;60% D2C-выручки, но&nbsp;его развитие намертво заблокировано чужим внешним бэклогом.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №2: Утечка конкурентных ноу-хау</h3>
        <p>Любые уникальные фичи и&nbsp;механики, протестированные вами, SaaS-провайдер упаковывает и&nbsp;продает вашим прямым конкурентам.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Риск №3: Архитектурная шизофрения</h3>
        <p>Две независимые админки, дублирование контента контент-менеджерами и&nbsp;хронический рассинхрон цен и&nbsp;остатков.</p>
      </div>
    </div>
  </div>
</section>
''',

    '09-HeadlessDeity.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_headless_shiva.jpg" alt="Headless Cyber Deity" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Headless: единый мозг и&nbsp;витрины</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Централизованный модульный бэкенд</h3>
        <p>PIM, промо-механики, ценообразование, единый профиль клиента и&nbsp;чекаут управляются строго из&nbsp;одной мастер-системы.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Равноправные клиентские каналы</h3>
        <ul style="margin-bottom: 0.6rem;">
          <li><strong>Web:</strong> молниеносный SSR-фронтенд с&nbsp;идеальным SEO</li>
          <li><strong>App:</strong> единый нативный код на&nbsp;Flutter под&nbsp;iOS и&nbsp;Android</li>
          <li><strong>МПК:</strong> омниканальное приложение для&nbsp;300+ розничных продавцов</li>
        </ul>
      </div>
      <div class="bullet-item glow-box border-green">
        <p>Принцип: настроил логику один раз&nbsp;— мгновенно применилось во&nbsp;всех каналах продаж.</p>
      </div>
    </div>
  </div>
</section>
''',

    '10-Democratization.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/deus_democratization.jpg" alt="Rebel Engineering Workshop" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Демократизация enterprise</h2>
    <h3 style="font-size: 1.55rem; color: var(--dim); margin-top: -1rem; margin-bottom: 1.5rem;">Как среднему бренду делать «по-взрослому»</h3>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Смена парадигмы разработки</h3>
        <p>Зрелые open-source решения позволяют небольшой команде развернуть архитектуру уровня лидеров рынка без&nbsp;гигантских бюджетов.</p>
      </div>
      <div class="bullet-item glow-box border-green">
        <h3 class="neon-green" style="font-size: 1.6rem; margin-bottom: 0.6rem;">Фактические метрики трансформации:</h3>
        <ul style="margin-bottom: 0;">
          <li>Снижение затрат на&nbsp;команду разработки в&nbsp;<strong>3&nbsp;раза</strong></li>
          <li>Ускорение вывода фич (Time-to-Market) в&nbsp;<strong>2—3&nbsp;раза</strong></li>
          <li>TCO платформы кратно ниже поддержки легаси и&nbsp;комиссий SaaS</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '11-OrgModel.astro': '''---
---
<section class="slide split-layout reverse">
  <div class="split-img">
    <img src="/images/deus_warhammer.jpg" alt="Exoskeleton AI Engineering Team" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Оргмодель «3&nbsp;человека + AI»</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Отказ от&nbsp;длинного плеча аутсорса</h3>
        <p>In-house спецназ: архитектор-CPO и&nbsp;два ведущих инженера работают в&nbsp;прямом бесшовном контакте с&nbsp;бизнесом без&nbsp;испорченного телефона.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">AI-экзоскелеты для&nbsp;производительности</h3>
        <p style="font-size: 1.35rem; margin-bottom: 0.5rem;">Боевое применение Cursor, Antigravity и&nbsp;Gemini на&nbsp;всех этапах:</p>
        <ul style="margin-bottom: 0;">
          <li>Глубокий аудит легаси-кода за&nbsp;часы вместо месяцев</li>
          <li>Автогенерация спецификаций, API-контрактов и&nbsp;схем БД</li>
          <li>Многократное ускорение прототипирования и&nbsp;тестов</li>
        </ul>
      </div>
    </div>
  </div>
</section>
''',

    '12-Cutover.astro': '''---
---
<section class="slide split-layout">
  <div class="split-img">
    <img src="/images/cyber_slums.jpg" alt="Slums vs New Spire parallel build" />
  </div>
  <div class="split-text">
    <h2 class="neon-cyan">Управление переходом: parallel build</h2>
    
    <div class="bullet-list">
      <div class="bullet-item">
        <h3 class="neon-magenta">Feature freeze старого контура</h3>
        <p>Жесткий мораторий на&nbsp;доработки монолита. Полный запрет инвестиций в&nbsp;код, который идет под&nbsp;снос.</p>
      </div>
      <div class="bullet-item">
        <h3 class="neon-magenta">Параллельное возведение платформы</h3>
        <p style="font-size: 1.35rem; margin-bottom: 0.5rem;">Старая система продолжает продавать, пока рядом строится новый контур:</p>
        <ul style="margin-bottom: 0.6rem;">
          <li><strong>Фаза 1:</strong> MVP (PIM, CMS, сверхбыстрый web-фронт)</li>
          <li><strong>Фаза 2:</strong> Core Commerce (бэкенд для&nbsp;Flutter-приложения)</li>
          <li><strong>Фаза 3:</strong> Scale (OMS, интеграция программы лояльности)</li>
        </ul>
      </div>
      <div class="bullet-item glow-box border-cyan">
        <p>Бесшовный cutover: мгновенное переключение без&nbsp;просадки продаж и&nbsp;потери SEO-трафика.</p>
      </div>
    </div>
  </div>
</section>
''',

    '13-QA.astro': '''---
---
<section class="slide title-slide" style="background-image: url('/images/deus_final_dawn.jpg');">
  <div class="title-overlay"></div>
  <div class="title-content flex-center text-center">
    <h1 class="glitch-text" style="font-size: 3.4rem; margin-bottom: 0.8rem; color: var(--pip-green);">Второе дыхание бизнеса</h1>
    <h2 style="font-size: 2.2rem; color: var(--sega-blue); margin-bottom: 0;">Вопросы и&nbsp;обсуждение</h2>
  </div>
  <div class="speaker-info-bottom">
    <span class="speaker-name">Илья Кадацкий</span>
    <span class="speaker-divider">|</span>
    <span class="speaker-event">FINN&nbsp;FLARE</span>
  </div>
</section>
'''
}

for name, content in slides.items():
    with io.open(os.path.join(slides_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully generated {len(slides)} slides v4.")
