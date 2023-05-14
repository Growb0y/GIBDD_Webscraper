
history_lists = {
        "typeOwner": {
            "Natural": "Физическое лицо",
            "Legal": "Юридическое лицо",
        },
        "typeAuto": {
            "01":"Грузовые автомобили бортовые",
            "02":"Грузовые автомобили шасси",
            "03":"Грузовые автомобили фургоны",
            "04":"Грузовые автомобили тягачи седельные",
            "05":"Грузовые автомобили самосвалы",
            "06":"Грузовые автомобили рефрижераторы",
            "07":"Грузовые автомобили цистерны",
            "08":"Грузовые автомобили с гидроманипулятором",
            "09":"Грузовые автомобили прочие",
            "21":"Легковые автомобили универсал",
            "22":"Легковые автомобили комби (хэтчбек)",
            "23":"Легковые автомобили седан",
            "24":"Легковые автомобили лимузин",
            "25":"Легковые автомобили купе",
            "26":"Легковые автомобили кабриолет",
            "27":"Легковые автомобили фаэтон",
            "28":"Легковые автомобили пикап",
            "29":"Легковые автомобили прочие",
            "41":"Автобусы длиной не более 5 м",
            "42":"Автобусы длиной более 5 м, но не более 8 м",
            "43":"Автобусы длиной более 8 м, но не более 12 м",
            "44":"Автобусы сочлененные длиной более 12 м",
            "49":"Автобусы прочие",
            "51":"Специализированные автомобили автоцистерны",
            "52":"Специализированные автомобили санитарные",
            "53":"Специализированные автомобили автокраны",
            "54":"Специализированные автомобили заправщики",
            "55":"Специализированные автомобили мастерские",
            "56":"Специализированные автомобили автопогрузчики",
            "57":"Специализированные автомобили эвакуаторы",
            "58":"Специализированные пассажирские транспортные средства",
            "59":"Специализированные автомобили прочие",
            "71":"Мотоциклы",
            "72":"Мотороллеры и мотоколяски",
            "73":"Мотовелосипеды и мопеды",
            "74":"Мотонарты",
            "80":"Прицепы самосвалы",
            "81":"Прицепы к легковым автомобилям",
            "82":"Прицепы общего назначения к грузовым автомобилям",
            "83":"Прицепы цистерны",
            "84":"Прицепы тракторные",
            "85":"Прицепы вагоны-дома передвижные",
            "86":"Прицепы со специализированными кузовами",
            "87":"Прицепы трейлеры",
            "88":"Прицепы автобуса",
            "89":"Прицепы прочие",
            "91":"Полуприцепы с бортовой платформой",
            "92":"Полуприцепы самосвалы",
            "93":"Полуприцепы фургоны",
            "95":"Полуприцепы цистерны",
            "99":"Полуприцепы прочие",
            "31":"Трактора",
            "32":"Самоходные машины и механизмы",
            "33":"Трамваи",
            "34":"Троллейбусы",
            "35":"Велосипеды",
            "36":"Гужевой транспорт",
            "38":"Подвижной состав железных дорог",
            "39":"Иной"
        },
        "typeOperation": {
            "01":"регистрация новых, произведенных в России или ввезенных, а также ввезенных в Россию бывших в эксплуатации, в том числе временно на срок более 6 месяцев, испытательной техники",
            "02":"регистрация ранее зарегистрированных в регистрирующих органах",
            "03":"изменение собственника (владельца)",
            "04":"изменение данных о собственнике (владельце)",
            "05":"изменение данных о транспортном средстве, в том числе изменение технических характеристик и (или) назначения (типа) транспортного средства",
            "06":"выдача взамен утраченных или пришедших в негодность государственных регистрационных знаков, регистрационных документов, паспортов транспортных средств.",
            "07":"прекращение регистрации в том числе",
            "08":"снятие с учета в связи с убытием за пределы Российской Федерации",
            "09":"снятие с учета в связи с утилизацией",
            "11":"первичная регистрация",
            "12":"регистрация снятых с учета",
            "13":"временная регистрация ТС (на срок проведения проверок, на срок временной прописки, регистрация испытательной техники)",
            "14":"временный учет (временная регистрация места пребывания ТС без выдачи документов)",
            "15":"регистрация ТС, ввезенных из-за пределов Российской Федерации",
            "16":"регистрация ТС, прибывших из других регионов Российской Федерации",
            "17":"регистрация ТС по новому месту жительства собственника, прибывшего из другого субъекта Российской Федерации, с одновременным снятием с учета по прежнему месту жительства",
            "18":"восстановление регистрации после аннулирования",
            "41":"замена государственного регистрационного знака",
            "42":"выдача дубликата регистрационного документа",
            "43":"выдача (замена) паспорта ТС",
            "44":"замена номерного агрегата, цвета, изменение конструкции ТС",
            "45":"изменение Ф.И.О. (наименования) владельца",
            "46":"изменение места жительства (юридического адреса) владельца в пределах территории обслуживания регистрационным пунктом",
            "47":"наличие запретов и ограничений",
            "48":"снятие запретов и ограничений",
            "49":"регистрация залога ТС",
            "50":"прекращение регистрации залога ТС",
            "51":"коррекция иных реквизитов",
            "52":"выдача акта технического осмотра",
            "53":"проведение ГТО",
            "54":"постоянная регистрация ТС по окончанию временной",
            "55":"коррекция реквизитов по информации налоговых органов",
            "56":"коррекция реквизитов при проведении ГТО",
            "61":"в связи с изменением места регистрации",
            "62":"в связи с прекращением права собственности (отчуждение, конфискация ТС)",
            "63":"в связи с вывозом ТС за пределы Российской Федерации",
            "64":"в связи с окончанием срока временной регистрации",
            "65":"в связи с утилизацией",
            "66":"в связи с признанием регистрации недействительной",
            "67":"снятие с временного учета",
            "68":"снятие с учета в связи с кражей или угоном",
            "69":"постановка с одновременным снятием с учета",
            "81":"документов в связи с обнаружением",
            "82":"удаление ошибочно введенной записи",
            "83":"удаление в связи со сверкой",
            "84":"перевод в архив в связи с корректировкой",
            "91":"по наследству с заменой государственных регистрационных знаков",
            "92":"по наследству с сохранением государственных регистрационных знаков за новым собственником (наследником)",
            "93":"по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с заменой государственных регистрационных знаков",
            "94":"по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с сохранением государственных регистрационных знаков за новым собственником"
        }
    }

replacing_dict = {
    "'AccidentDateTime'": "'Дата и время ДТП'",
    "'AccidentType'": "'Тип ДТП'",
    "'AccidentPlace'": "'Место ДТП'",
    "'DamageDestription'": "'Описание повреждения'",
    "'RegionName'": "'Регион ДТП'",
    "'VehicleMark'": "'Марка авто'",
    "'VehicleAmount'": "'Кол-во участников ДТП'",
    "'VehicleModel'": "'Модель авто'",
    "'VehicleYear'": "'Год выпуска авто'",
    "'VehicleDamageState'": "'Состояние авто'",
    "'from'": "'От'",
    "'to'": "'До'",
    "'simplePersonType'": "'Тип владельца'",
    "'Legal'": "'юридическое лицо'",
    "'Natural'": "'физическое лицо'",
    "'lastOperation': '01'":"'Последняя операция': 'регистрация новых, произведенных в России или ввезенных, а также ввезенных в Россию бывших в эксплуатации, в том числе временно на срок более 6 месяцев, испытательной техники'",
    "'lastOperation': '02'":"'Последняя операция': 'регистрация ранее зарегистрированных в регистрирующих органах'",
    "'lastOperation': '03'":"'Последняя операция': 'изменение собственника (владельца)'",
    "'lastOperation': '04'":"'Последняя операция': 'изменение данных о собственнике (владельце)'",
    "'lastOperation': '05'":"'Последняя операция': 'изменение данных о транспортном средстве, в том числе изменение технических характеристик и (или) назначения (типа) транспортного средства'",
    "'lastOperation': '06'":"'Последняя операция': 'выдача взамен утраченных или пришедших в негодность государственных регистрационных знаков, регистрационных документов, паспортов транспортных средств.'",
    "'lastOperation': '07'":"'Последняя операция': 'прекращение регистрации в том числе'",
    "'lastOperation': '08'":"'Последняя операция': 'снятие с учета в связи с убытием за пределы Российской Федерации'",
    "'lastOperation': '09'":"'Последняя операция': 'снятие с учета в связи с утилизацией'",
    "'lastOperation': '11'":"'Последняя операция': 'первичная регистрация'",
    "'lastOperation': '12'":"'Последняя операция': 'регистрация снятых с учета'",
    "'lastOperation': '13'":"'Последняя операция': 'временная регистрация ТС (на срок проведения проверок, на срок временной прописки, регистрация испытательной техники)'",
    "'lastOperation': '14'":"'Последняя операция': 'временный учет (временная регистрация места пребывания ТС без выдачи документов)'",
    "'lastOperation': '15'":"'Последняя операция': 'регистрация ТС, ввезенных из-за пределов Российской Федерации'",
    "'lastOperation': '16'":"'Последняя операция': 'регистрация ТС, прибывших из других регионов Российской Федерации'",
    "'lastOperation': '17'":"'Последняя операция': 'регистрация ТС по новому месту жительства собственника, прибывшего из другого субъекта Российской Федерации, с одновременным снятием с учета по прежнему месту жительства'",
    "'lastOperation': '18'":"'Последняя операция': 'восстановление регистрации после аннулирования'",
    "'lastOperation': '41'":"'Последняя операция': 'замена государственного регистрационного знака'",
    "'lastOperation': '42'":"'Последняя операция': 'выдача дубликата регистрационного документа'",
    "'lastOperation': '43'":"'Последняя операция': 'выдача (замена) паспорта ТС'",
    "'lastOperation': '44'":"'Последняя операция': 'замена номерного агрегата, цвета, изменение конструкции ТС'",
    "'lastOperation': '45'":"'Последняя операция': 'изменение Ф.И.О. (наименования) владельца'",
    "'lastOperation': '46'":"'Последняя операция': 'изменение места жительства (юридического адреса) владельца в пределах территории обслуживания регистрационным пунктом'",
    "'lastOperation': '47'":"'Последняя операция': 'наличие запретов и ограничений'",
    "'lastOperation': '48'":"'Последняя операция': 'снятие запретов и ограничений'",
    "'lastOperation': '49'":"'Последняя операция': 'регистрация залога ТС'",
    "'lastOperation': '50'":"'Последняя операция': 'прекращение регистрации залога ТС'",
    "'lastOperation': '51'":"'Последняя операция': 'коррекция иных реквизитов'",
    "'lastOperation': '52'":"'Последняя операция': 'выдача акта технического осмотра'",
    "'lastOperation': '53'":"'Последняя операция': 'проведение ГТО'",
    "'lastOperation': '54'":"'Последняя операция': 'постоянная регистрация ТС по окончанию временной'",
    "'lastOperation': '55'":"'Последняя операция': 'коррекция реквизитов по информации налоговых органов'",
    "'lastOperation': '56'":"'Последняя операция': 'коррекция реквизитов при проведении ГТО'",
    "'lastOperation': '61'":"'Последняя операция': 'в связи с изменением места регистрации'",
    "'lastOperation': '62'":"'Последняя операция': 'в связи с прекращением права собственности (отчуждение, конфискация ТС)'",
    "'lastOperation': '63'":"'Последняя операция': 'в связи с вывозом ТС за пределы Российской Федерации'",
    "'lastOperation': '64'":"'Последняя операция': 'в связи с окончанием срока временной регистрации'",
    "'lastOperation': '65'":"'Последняя операция': 'в связи с утилизацией'",
    "'lastOperation': '66'":"'Последняя операция': 'в связи с признанием регистрации недействительной'",
    "'lastOperation': '67'":"'Последняя операция': 'снятие с временного учета'",
    "'lastOperation': '68'":"'Последняя операция': 'снятие с учета в связи с кражей или угоном'",
    "'lastOperation': '69'":"'Последняя операция': 'постановка с одновременным снятием с учета'",
    "'lastOperation': '81'":"'Последняя операция': 'документов в связи с обнаружением'",
    "'lastOperation': '82'":"'Последняя операция': 'удаление ошибочно введенной записи'",
    "'lastOperation': '83'":"'Последняя операция': 'удаление в связи со сверкой'",
    "'lastOperation': '84'":"'Последняя операция': 'перевод в архив в связи с корректировкой'",
    "'lastOperation': '91'":"'Последняя операция': 'по наследству с заменой государственных регистрационных знаков'",
    "'lastOperation': '92'":"'Последняя операция': 'по наследству с сохранением государственных регистрационных знаков за новым собственником (наследником)'",
    "'lastOperation': '93'":"'Последняя операция': 'по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с заменой государственных регистрационных знаков'",
    "'lastOperation': '94'":"'Последняя операция': 'по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с сохранением государственных регистрационных знаков за новым собственником'"
}

needed_indexes_dtp = ['Дата и время ДТП', 'Тип ДТП', 'Место ДТП', 'Регион ДТП', 'Кол-во участников ДТП', 'Описание повреждения', 'Состояние авто', 'Марка авто', 'Модель авто', 'Год выпуска авто', 'VehicleSort']
needed_indexes_history = ['От', 'До', 'Тип владельца', 'Последняя операция']

russian_to_english = {
    'А': 'A',
    'В': 'B',
    'Е': 'E',
    'К': 'K',
    'М': 'M',
    'Н': 'H',
    'О': 'O',
    'Р': 'P',
    'С': 'C',
    'Т': 'T',
    'У': 'Y',
    'Х': 'X',
}
