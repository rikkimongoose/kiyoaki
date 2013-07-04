#!/usr/bin/python 
# -*- coding: utf-8 -*-

DEFAULT_SURNAMES = [
    "Авин",
    "Авчинник",
    "Аксамит",
    "Алампиев",
    "Алещенко",
    "Андреенко",
    "Андрейченко",
    "Анисенко",
    "Антоненко",
    "Антончик",
    "Апацкий",
    "Арцименя",
    "Бамбиза",
    "Барановский",
    "Бардовский",
    "Барсуков",
    "Бедулин",
    "Беленький",
    "Белый",
    "Бердавцев",
    "Бедулин",
    "Боборыкина",
    "Бобоченок",
    "Боговцов",
    "Бойко",
    "Бокач",
    "Болотин",
    "Борис",
    "Борисенко",
    "Борщ",
    "Борщевский",
    "Бочаров",
    "Бродский",
    "Бубневич",
    "Булахов",
    "Бурачков",
    "Василевский",
    "Васильев",
    "Вашкевич",
    "Величко",
    "Вертинский",
    "Веслоухов",
    "Вечерский",
    "Власенко",
    "Внучко",
    "Войтенков",
    "Войтешик",
    "Волков",
    "Волчецкий",
    "Воробей",
    "Гаркун",
    "Гацко",
    "Герасименко",
    "Герасимов",
    "Герасюк",
    "Герменчук",
    "Гетц",
    "Гилевич",
    "Глушкевич",
    "Голубев",
    "Голубович",
    "Гончар",
    "Гончарик",
    "Горелик",
    "Гриб",
    "Грибанов",
    "Грибач",
    "Гринев",
    "Грушевой",
    "Гушель",
    "Гюнтер",
    "Давидович",
    "Давлюд",
    "Данилевич",
    "Даниленко",
    "Дворянинович",
    "Дегтярев",
    "Дейко",
    "Дементей",
    "Демиденко",
    "Дзичковский",
    "Долголев",
    "Долженков",
    "Домашкевич",
    "Доменикан",
    "Драган",
    "Дражин",
    "Дробышевская",
    "Дробышевский",
    "Дубовский",
    "Дубынин",
    "Евлашов",
    "Ермолаев",
    "Жебрак",
    "Жидиляев",
    "Жук",
    "Жукович",
    "Жуковский",
    "Журавлев",
    "Заблоцкий",
    "Завадский",
    "Зайцев",
    "Зарецкий",
    "Захаренко",
    "Зверев",
    "Зданевич",
    "Зеленин",
    "Зеленин",
    "Иванов",
    "Ивашкевич",
    "Извалова",
    "Казючиц",
    "Каковка",
    "Калмычков",
    "Камай",
    "Карпенко",
    "Карпов",
    "Катушкин",
    "Качан",
    "Кебич",
    "Кеник",
    "Кичкайло",
    "Ковалев",
    "Ковалев",
    "Ковалёнок",
    "Коваль",
    "Козик",
    "Козлов",
    "Козяк",
    "Кокореко",
    "Колбаско",
    "Колодко",
    "Комар",
    "Коновалов",
    "Конопля",
    "Концевич",
    "Конюшик",
    "Копач",
    "Копытов",
    "Корнеенко",
    "Николай Фомич",
    "Коротченя",
    "Корявко",
    "Котов",
    "Кравченко",
    "Кривецкий",
    "Кришталевич",
    "Крупник",
    "Крыжановский",
    "Кудлаш",
    "Кудрявец",
    "Кузменков",
    "Кузнецов",
    "Кузнецов",
    "Кузьма",
    "Кузюк",
    "Кулаженко",
    "Кулаков",
    "Куличков",
    "Курбаев",
    "Курдюков",
    "Кучинский",
    "Лавицкий",
    "Лазаревич",
    "Лазебник",
    "Лактюшин",
    "Лапоухов",
    "Лебедько",
    "Левчик",
    "Леонов",
    "Летко",
    "Литвинов",
    "Лобач",
    "Лобко",
    "Ломать",
    "Лужинский",
    "Лукашев",
    "Лукашенко",
    "Любовицкий",
    "Макаревич",
    "Макейченко",
    "Малаховский",
    "Малашко",
    "Малышев",
    "Мамчиц",
    "Маринич",
    "Маркевич",
    "Марковский",
    "Мартос",
    "Матюшевский",
    "Матюшонок",
    "Мацкевич",
    "Мачуленко",
    "Медведев",
    "Милованов",
    "Минченко",
    "Минько",
    "Митько",
    "Моисеев",
    "Мордашов",
    "Морозов",
    "Мошко",
    "Мяделец",
    "Мять",
    "Наумчик",
    "Некрасов",
    "Нелюбин",
    "Нетылькин",
    "Никитин",
    "Никончук",
    "Новик",
    "Новиков",
    "Новиков",
    "Новиков",
    "Образов",
    "Обухов",
    "Овечкин",
    "Павлов",
    "Павловский",
    "Палагеча",
    "Паруль",
    "Оппозиция",
    "Парфенюк",
    "Пахилко",
    "Пенькова",
    "Писаревич",
    "Пискарев",
    "Пискунов",
    "Плотский",
    "Позняк",
    "Позюмко",
    "Попков",
    "Попов",
    "Попов",
    "Похолок",
    "Привалов",
    "Прищеп",
    "Прокопов",
    "Прокопович",
    "Протас",
    "Пырх",
    "Радецкий",
    "Радкевич",
    "Радомысльский",
    "Рахатко",
    "Русак",
    "Русакевич",
    "Руцкий",
    "Савицкий",
    "Садовский",
    "Саенко",
    "Сакович",
    "Самойленко",
    "Самощев",
    "Самусевич",
    "Сапранецкий",
    "Сапронов",
    "Селивончик",
    "Семашко",
    "Семдянова",
    "Сердюк",
    "Середа",
    "Середич",
    "Сечко",
    "Сивицкий",
    "Сивицкий",
    "Сивчиков",
    "Синицын",
    "Синчилин",
    "Скоробогатько",
    "Скорынин",
    "Скрицкий",
    "Слабченко",
    "Слемнев",
    "Слесарь",
    "Слобода",
    "Смоляр",
    "Соколов",
    "Соколов",
    "Солдатов",
    "Солдатова",
    "Сорокин",
    "Соснов",
    "Сосновский",
    "Спиглазов",
    "Станкевич",
    "Степаненко",
    "Студенцов",
    "Судас",
    "Сукач",
    "Сумар",
    "Сушкевич",
    "Сырокваш",
    "Тарасенко",
    "Тележников",
    "Терешко",
    "Тесовец",
    "Титенков",
    "Титков",
    "Титов",
    "Тихиня",
    "Тихонов",
    "Тишкевич",
    "Толстик",
    "Торманов",
    "Третьяков",
    "Трофименко",
    "Трусов",
    "Трухан",
    "Турок",
    "Удовиков",
    "Улитина",
    "Уренюк",
    "Устинович",
    "Фарфель",
    "Федоренко",
    "Федорчук",
    "Флорьянович",
    "Фрейберг",
    "Хвощ",
    "Хейдоров",
    "Хитрик",
    "Холод",
    "Холщевников",
    "Цумаров",
    "Чеваньков",
    "Чекушев",
    "Чепик",
    "Черныш",
    "Чех",
    "Чирун",
    "Чувичко",
    "Чура",
    "Шабашов",
    "Шарко",
    "Шачек",
    "Оппозиция",
    "Шашков",
    "Шевнин",
    "Шевцов",
    "Шейман",
    "Шидловец",
    "Шилько",
    "Шимчук",
    "Шипко",
    "Шкапич",
    "Шкурко",
    "Шолодонов",
    "Штокин",
    "Шут",
    "Шушкевич",
    "Юркевич",
    "Якобсон",
    "Якубец",
    "Якубовский",
    "Янец",
    "Яскевич",
    "Ястреб",
    "Вахромеев",
    "Абрамова",
    "Азарченков",
    "Александров",
    "Александрович",
    "Алексеенко",
    "Ананьев",
    "Аникеев",
    "Анушкин",
    "Аполоник",
    "Астапкович",
    "Астапченко",
    "Афанасьев",
    "Бань",
    "Башаримов",
    "Бекиш",
    "Белов",
    "Белькович",
    "Беляков",
    "Биккинин",
    "Бич",
    "Блюдник",
    "Бобков",
    "Богданкевич",
    "Боярчук",
    "Бруцкий",
    "Бурак",
    "Бусел",
    "Бусько",
    "Бухвостов",
    "Валаханович",
    "Вараницкий",
    "Винокурова",
    "Войтехович",
    "Волженков",
    "Волков",
    "Волков",
    "Воронович",
    "Ворошнин",
    "Вронский",
    "Гаргун",
    "Герасименко",
    "Гируть",
    "Глуховский",
    "Говорушкин",
    "Гончар",
    "Гончарик",
    "Горбунов",
    "Гриб",
    "Григорьев",
    "Грунтов",
    "Грушевский",
    "Грязнова",
    "Гуков",
    "Демидов",
    "Дмуховский",
    "Добровольский",
    "Домаш",
    "Донейко",
    "Драко",
    "Дубко",
    "Дубовик",
    "Дудко",
    "Дунич",
    "Дылевский",
    "Егоров",
    "Енко",
    "Жушма",
    "Завадский",
    "Зайцев",
    "Замковенко",
    "Зданчук",
    "Здобнов",
    "Зинченко",
    "Знавец",
    "Игнатищев",
    "Калугин",
    "Калякин",
    "Камай",
    "Капшай",
    "Карпенко",
    "Карпиевич",
    "Кашкан",
    "Кебич",
    "Киберман",
    "Киреев",
    "Климов",
    "Кожан",
    "Козловский",
    "Козырь",
    "Койда",
    "Комяк",
    "Конашук",
    "Коноплев",
    "Коротченя",
    "Костян",
    "Котляров",
    "Кравченко",
    "Красуцкий",
    "Круговой",
    "Крючков",
    "Кудинов",
    "Кузьма",
    "Кулаковский",
    "Кулик",
    "Куцко",
    "Кучинский",
    "Лапковский",
    "Лапуть",
    "Лебедько",
    "Левшик",
    "Лекторов",
    "Лещинский",
    "Лившиц",
    "Липкин",
    "Литвин",
    "Лозовик",
    "Лукьянович",
    "Лунович",
    "Любезный",
    "Любовицкий",
    "Майструк",
    "Малаховский",
    "Малофеев",
    "Малумов",
    "Манукова",
    "Мельников",
    "Миколуцкий",
    "Минич",
    "Мирголовский",
    "Михадюк",
    "Невестенко",
    "Нистюк",
    "Новак",
    "Новиков",
    "Новосяд",
    "Папруга",
    "Пасечник",
    "Пашкевич",
    "Пинчук",
    "Плетюхов",
    "Побяржин",
    "Погорельский",
    "Полочанин",
    "Понкратенко",
    "Попченко",
    "Почепко",
    "Прокопович",
    "Прокошин",
    "Прохорчик",
    "Пугачев",
    "Пыжик",
    "Радкевич",
    "Рачков",
    "Римарчик",
    "Рожко",
    "Розганов",
    "Розынко",
    "Романовский",
    "Руденко",
    "Руммо",
    "Рускевич",
    "Савичев",
    "Сакович",
    "Самусева",
    "Свирид",
    "Свирид",
    "Сечко",
    "Скок",
    "Скриган",
    "Снегирь",
    "Соловьев",
    "Сосонко",
    "Тарасевич",
    "Телебук",
    "Тереня",
    "Терешко",
    "Терещенко",
    "Тютюнов",
    "Усюкевич",
    "Ходневич",
    "Ходосевич",
    "Хомич",
    "Хрол",
    "Худая",
    "Шарецкий",
    "Шаршунов",
    "Шевцов",
    "Шиманский",
    "Шлындиков",
    "Шпаков",
    "Шпилевский",
    "Шуляковский",
    "Шушкевич",
    "Щукин",
    "Юнчик",
    "Юхимук",
    "Якобсон",
    "Яковчик",
    "Янович"
]

DEFAULT_SURNAMES_FIXES = [
    (r"a", "ыыыы")
]

if __name__ == "__main__":
    print "Surnames base file for Kiyoaki generator. The default surnames are:\n\n"
    for surname in DEFAULT_SURNAMES:
        print surname
