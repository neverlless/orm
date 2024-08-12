usersTempQuests = {}


async def giveQuest(user, name):
    if name == 'Я просто хотел выпить...':
        descr = "Одним поздним вечером, после того как боль от клейма на заднице начала затухать, ты решил немного выпить, но не тут-то было - бармен говорит про вступительный взнос который составляет 1🔘Очко прокачки. Речь ведь про ПРОКАЧКУ, ДА?"
        text = "Отдать 1🔘 бармену"
    elif name == 'Богиня Хэвенбурга':
        descr = "Добро пожаловать в Хэвенбург! Ты уже познакомился с местной богиней? Её зовут Раскулова и у многих в этом городе мощнейшая эрекция от её взгляда. Даже у девочек... КХМ! Суть то в чём - она попросила тебя найти её нижнее бельё. Возможно, есть смысл поискать вне города или же поспрашивать у членов своей группировки..."
        text = "Отдать 👙Нижнее бельё Раскуловой"
    elif name == 'Скупщик. Знакомство':
        descr = "Бомж на площади весьма юморной - его жене пора в гроб, а он хочет ей подкинуть положительный тест на беременность. Ну даёт мужик, респект! Но нужно еще и найти этот тест... Судя по разговорам школьников, тусовавшихся на площади недалеко, найти можно их у изгнанных школьниц в Случайном лесу. Что же, если это единственный вариант..."
        text = "Отдать 🌡Положительный тест на беременность бомжу"
    elif name == 'Хрен с горы':
        descr = "Конечно ты ненавидишь быдло, его никто не любит. Но это полезное быдло. Увы, придётся дать ему парочку очков репутации. Что? Очки репутации? Не обращай внимания. Давай лучше сходим и найдём эту чешую. Как я понял, она падает в локациях Хэвенбурга."
        text = "Дать 🔻Багровую чешую Драконоборцу на пробу."
    elif name == 'Мастер на все руки':
        descr = "Весьма прямолинейный мужик, а еще я сомневаюсь что он использует эту всю одежду по предназначению... 🧊Снунец можно найти у монстров Заснеженного леса, есть смысл идти у него на поводу?"
        text = "Дать 🧊Снунец Лысему на пробу."
    elif name == 'Элитный бар для элиты':
        descr = "Носить трусы ходячему сексу было точно лучше, чем собирать сейчас эту сотню 🧊Снунцев... Искать её нужно в Заснеженном лесу."
        text = "Заплатить взнос в размере 100 🧊Снунцов охране элитного бара"
    plusText = "\n\n⚠️Получено задание - {}.\nУсловие: {}".format(name, text)
    newQuest = await db.Quests(idplayer=user.id, status=1, name=name, descr=descr)
    await newQuest.save()
    return plusText



async def quests(m, user):
    if m.from_user.id != m.chat.id: return
    if user:
        text = "Активные задания:\n"
        if user.scenarioStatus != 0:
            text += "❗️Основное задание:\n"
            if user.scenario == 1: text += "Найти Заброшенный архив в Лесной гробнице, что находится в глуби Случайного Леса\n"
            elif user.scenario == 2 and user.scenarioStatus == 1: text += "Исследовать ⛩Алтари в песчаной пирамиде\n"
            elif user.scenario == 2 and user.scenarioStatus == 2: text += "Получить награду\n"
            elif user.scenario == 2 and user.scenarioStatus == 3: text += "Зачистить пирамиду до конца\n"
            elif user.scenario == 2 and user.scenarioStatus == 4: text += "Получить награду\n"
            elif user.scenario == 3 and user.scenarioStatus == 1: text += "Отнести бомжу по 10 материалов улучшения оружия\n"
            elif user.scenario == 3 and user.scenarioStatus == 2: text += "Получить награду на следующий день\n"
            elif user.scenario == 3 and user.scenarioStatus == 3: text += "Забрать награду\n"
            elif user.scenario == 3 and user.scenarioStatus == 4: text += "Подойти к бомжу на следующий день\n"
            elif user.scenario == 3 and user.scenarioStatus == 5: text += "Обратиться к бомжу\n"
            elif user.scenario == 3 and user.scenarioStatus == 6: text += "Отдать бомжу 50🔻\n"
            elif user.scenario == 3 and user.scenarioStatus == 7: text += "Подойти к бомжу на следующий день\n"
            elif user.scenario == 3 and user.scenarioStatus == 8: text += "Подойти к бомжу\n"
            elif user.scenario == 3 and user.scenarioStatus == 9: text += "Найти Клару в Гробнице\n"
            elif user.scenario == 4 and user.scenarioStatus == 0: text += "Зарядить заготовку\n"
            elif user.scenario == 4: text += "???\n"
            elif user.scenario == 5 and user.scenarioStatus == 0: text += "Обратиться за советом к охраннику\n"
            elif user.scenario == 5 and user.scenarioStatus == 1: text += "Отыскать осведомителя в Кавайне\n"
            elif user.scenario == 5 and user.scenarioStatus == 2: text += "Оплатить осведомителю услугу двумя зельями сопротивления холоду\n"
            elif user.scenario == 5 and user.scenarioStatus == 3: text += "Подождать до завтра\n"
            elif user.scenario == 5 and user.scenarioStatus == 4: text += "Доплатить осведомителю двумя зельями сопротивления холоду\n"
            elif user.scenario == 5 and user.scenarioStatus == 5: text += "Отнести 5 Чернил\n"
            elif user.scenario == 5 and user.scenarioStatus == 6: text += "Дождаться следующего дня\n"
            elif user.scenario == 5 and user.scenarioStatus == 7: text += "Отправиться к Осведомителю\n"
            elif user.scenario == 5 and user.scenarioStatus == 8: text += "Отправиться по следам отряда учёных\n"
            elif user.scenario == 5 and user.scenarioStatus == 9: text += "Вернуться к Осведомителю\n"
            elif user.scenario == 5 and user.scenarioStatus == 10: text += "Заплатить 500🧊 и 50🔻 учёному через Осведомителя\n"
            elif user.scenario == 5 and user.scenarioStatus == 11: text += "???\n"
            else: text += "Отсутствует\n"
        allQuests = await db.Quests.filter(idplayer=user.id, status=1)
        if allQuests:
            text += "\nДругие:"
            for z in allQuests:
                text += "\n{} (/questInfo_{})".format(z.name, z.id)
        if user.questStatus != 0:
            text += "\n\nЗадание охранника: {}. Подробнее у охранника.".format(user.quest)
        await bot.send_message(m.chat.id, text)

@dp.message_handler(lambda m:m.text and m.text.startswith('/questInfo_'))
async def questInfo(m):
    if m.from_user.id != m.chat.id:
        return
    result = m.text.replace('/questInfo_', '', 1).replace('@TowerOfHeaven_bot', '', 1)
    player = await db.Users.get(user_id=m.from_user.id)
    if player:
        getQuest = await db.Quests.get_or_none(id=result)
        if getQuest and getQuest.idplayer == player.id and getQuest.status == 1:
            await bot.send_message(m.chat.id, "{}. {}".format(getQuest.name, getQuest.descr))
        else:
            return







########################
##########DAILY#########
########################
async def questsglobal(user):
    if user.questId == 7 and user.questStatus == 1:
        await bot.edit_message_text("Пока работы нет, извиняй...", call.message.chat.id, call.message.message_id)
        status = 0
        return status
    if user.lvl >= 7:
        status = 0
        randomQuests = ['Убийца', 'Искатель приключений', 'Азартный путник', 'Поставщик', 'Качок', 'Продаван', 'Поставщик одуванчиков', 'Поставщик роз', 'Поставщик костей']
        if user.frak and user.frak != "":
            randomQuests.append('Небесный властелин')
        if user.lvl >= 25:
            randomQuests.append('Экспедитор')
        if user.questId < 10:
            user.questStatus = 0
            user.questId = 11
            user.quest = ''
        if user.questStatus == 0:
            try:
                if user.dailyBP == 1:
                    text = "Ты подошел к охраннику, но он лишь покачал головой, мол, работы пока нет. Приходи завтра"
                    return text, status
                else:
                    user.quest = random.choice(randomQuests)
                    if user.quest == 'Убийца': text = 'О, здаров... Короче, для тебя сегодня очень важное задание - активность монстров вне города резко увеличилась сегодня, поэтому тебе мы даём самое отвественное задание - уничтожь 60 мобов. Потом вернёшься за наградой.'
                    elif user.quest == 'Всемогущий': text = 'Слышал про новую доску в городе? Там какие-то очки славы даются и всё в таком духе. Так вот, я хочу чтобы ты тоже отличился, как мой ученик! Победи трёх других людей, только сильно их там не уничтожай...'
                    elif user.quest == 'Небесный властелин': text = 'Ооооо, какой хороший день - лучший, я считаю, день для захвата башни... О, а вот и ты. Я хочу чтобы ты захватил со своей группировкой этаж в башне. Не подведи!'
                    elif user.quest == 'Искатель приключений': text = 'Какие люди! Я тут тебя уже заждался. Сегодня для тебя самое неприятное задание, я считаю... Нужно исходить весь лес вдоль и поперёк. А если быть точнее, проверить ближайшие 100 клеток (без смертей). Ну, не подведи, комрад.'
                    elif user.quest == 'Азартный путник': text = 'Опа, ну типа привет. Пошли на деньги сыграем, с тебя 3 победы!'
                    elif user.quest == 'Поставщик': text = 'Нет времени обьяснять - бери весь хлам что у тебя есть и дуй бомжу сливай! Я тебе немного отсыплю за это.'
                    elif user.quest == 'Качок': text = 'Йо. У меня подписан контракт с местной сетью качалок и я предлагаю тебе прокачаться минимум на 1000💰.'
                    elif user.quest == 'Продаван': text = 'Дарова, чел! Пора тебя немного поэксплуатировать - нам нужно развитие рынка, поэтому продай в Раскуловой около трёх вещей.'
                    elif user.quest == 'Экспедитор': text = 'Какие люди в Хэвенбурге! Как сам вообще? Давно тебя не видел. Но, увы, у меня для тебя сразу же есть задание. Тебе необходимо сгонять в экспедицию - это принесёт прибыль и тебе и мне! Ну, что скажешь?'
                    elif user.quest == 'Поставщик роз': text = 'Давненько не виделись. Ну, как дела? Живёшь, процветаешь? Короче тут такое дело... Хочу жене своей букет подарить, не мог бы ты помочь? Мне нужно 25 роз.'
                    elif user.quest == 'Поставщик одуванчиков': text = 'Хехе, а вот и главный алкаш города! Здоровеньки были, я по твоей любимой теме. В одной книге про какой-то импакт писалось про классное вино из одуванчиков. Ну, вот хочу проверить. Принесёшь 25 одуванчиков?'
                    elif user.quest == 'Поставщик костей': text = 'С добрым утром! А? Уже не утро? Да откуда мне знать какой у тебя часовой пояс. Тут такое дело - у меня кости кончились, а зелья варить надо, ну вообще не вариант эти на 50❤️ варить... Есть 10 костей?'
                    elif user.quest == 'Уровнеподъёмщик': text = 'Хо-хо, какие люди ко мне пораньше пришли! Хотел задание? Давай так - ты поднимаешь уровень, а я уж в долгу не останусь!'
                    elif user.quest == 'Пряточка': text = 'Ууух, как же ты вовремя! Я подписал контракт с домом Адского, поэтому твоя задача на этот день - сыграть там в прятки. Так что дерзай, легчайшие деньги.'
                    addQuest = await db.tempQuest(user_id=user.user_id, quest=user.quest, progress=0, status = 0)
                    await addQuest.save()
                    user.questStatus = 1
                    await user.save()
                    status = 1
            except:
                if user.questStatus == 0:
                    user.quest = random.choice(randomQuests)
                    if user.quest == 'Убийца': text = 'О, здаров... Короче, для тебя сегодня очень важное задание - активность монстров вне города резко увеличилась сегодня, поэтому тебе мы даём самое отвественное задание - уничтожь 60 мобов. Потом вернёшься за наградой.'
                    elif user.quest == 'Всемогущий': text = 'Слышал про новую доску в городе? Там какие-то очки славы даются и всё в таком духе. Так вот, я хочу чтобы ты тоже отличился, как мой ученик! Победи трёх других людей, только сильно их там не уничтожай...'
                    elif user.quest == 'Небесный властелин': text = 'Ооооо, какой хороший день - лучший, я считаю, день для захвата башни... О, а вот и ты. Я хочу чтобы ты захватил со своей группировкой хотя бы один этаж в башне. Не подведи!'
                    elif user.quest == 'Искатель приключений': text = 'Какие люди! Я тут тебя уже заждался. Сегодня для тебя самое неприятное задание, я считаю... Нужно исходить весь лес вдоль и поперёк. А если быть точнее, проверить ближайшие 100 клеток (без смертей). Ну, не подведи, комрад.'
                    elif user.quest == 'Азартный путник': text = 'Опа, ну типа привет. Пошли на деньги сыграем, с тебя 3 победы!'
                    elif user.quest == 'Поставщик': text = 'Нет времени обьяснять - бери весь хлам что у тебя есть и дуй бомжу сливай! Я тебе немного отсыплю за это.'
                    elif user.quest == 'Ключевод': text = 'Приветики. Слыхал что на северной стороне города собираются открыть ворота? Советую тебе внести свой вклад в это дело - вставь ключик.'
                    elif user.quest == 'Качок': text = 'Йо. У меня подписан контракт с местной сетью качалок и я предлагаю тебе прокачаться минимум на 1000💰.'
                    elif user.quest == 'Продаван': text = 'Дарова, чел! Пора тебя немного поэксплуатировать - нам нужно развитие рынка, поэтому продай в Раскуловой около трёх вещей.'
                    elif user.quest == 'Экспедитор': text = 'Какие люди в Хэвенбурге! Как сам вообще? Давно тебя не видел. Но, увы, у меня для тебя сразу же есть задание. Тебе необходимо сгонять в экспедицию - это принесёт прибыль и тебе и мне! Ну, что скажешь?'
                    elif user.quest == 'Поставщик роз': text = 'Давненько не виделись. Ну, как дела? Живёшь, процветаешь? Короче тут такое дело... Хочу жене своей букет подарить, не мог бы ты помочь? Мне нужно 25 роз.'
                    elif user.quest == 'Поставщик одуванчиков': text = 'Хехе, а вот и главный алкаш города! Здоровеньки были, я по твоей любимой теме. В одной книге про какой-то импакт писалось про классное вино из одуванчиков. Ну, вот хочу проверить. Принесёшь 25 одуванчиков?'
                    elif user.quest == 'Поставщик костей': text = 'С добрым утром! А? Уже не утро? Да откуда мне знать какой у тебя часовой пояс. Тут такое дело - у меня кости кончились, а зелья варить надо, ну вообще не вариант эти на 50❤️ варить... Есть 10 костей?'
                    elif user.quest == 'Уровнеподъёмщик': text = 'Хо-хо, какие люди ко мне пораньше пришли! Хотел задание? Давай так - ты поднимаешь уровень, а я уж в долгу не останусь!'
                    elif user.quest == 'Пряточка': text = 'Ууух, как же ты вовремя! Я подписал контракт с домом Адского, поэтому твоя задача на этот день - сыграть там в прятки. Так что дерзай, легчайшие деньги.'
                    addQuest = await db.tempQuest(user_id=user.user_id, quest=user.quest, progress=0, status = 0)
                    await addQuest.save()
                    user.questStatus = 1
                    await user.save()
                    status = 1
        elif user.quest in randomQuests and user.questStatus == 1:
            if user.quest == 'Убийца':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 60:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 15
                    user.questStatus = 0
                    user.slava += 5
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    awardText = ""
                    text = "Угу-угу, я наслышал о твоих битвах уже. Держи награду\nПолучено 15🏷\n\n{}".format(awardText)
                else:
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - уничтожить 60 монстров. У тебя же готово только {}".format(quest.progress)
                    status = 1
            elif user.quest == 'Всемогущий':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 3:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 5
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Угу-угу, я наслышал о твоих битвах уже. Держи награду\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - победить в 3х битвах против других людей. У тебя же только {} побед".format(quest.progress)
            elif user.quest == 'Небесный властелин':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 1:
                    quest.timeEnd = time.time() + 86400
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    user.coupon += 20
                    user.questStatus = 0
                    user.slava += 4
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Угу-угу, я наслышал о твоих битвах уже. Держи награду\nПолучено 20🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - захватить этаж в башне"
            elif user.quest == 'Искатель приключений':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 100:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 15
                    user.questStatus = 0
                    user.slava += 5
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Угу-угу, я наслышал о твоих битвах уже. Держи награду\nПолучено 15🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - пройти 100 клеток. У тебя же готово только {}".format(quest.progress)
            elif user.quest == 'Азартный путник':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 3:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 2
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Угу-угу, я наслышал о твоих победах уже. Держи награду\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - победить три раза в казино. У тебя же готово только {}".format(quest.progress)
            elif user.quest == 'Поставщик':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 5:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 4
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Да-да, спасибо за помощь. Держи награду\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - продать 5 ед товара бомжу. У тебя же готово только {}".format(quest.progress)
            elif user.quest == 'Качок':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 1000:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 15
                    user.questStatus = 0
                    user.slava += 2
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Делаешь вклад в саморазвитие. Держи награду\nПолучено 15🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - прокачаться хотя бы на тысячу💰. Ты же прокачался на {}💰".format(quest.progress)
            elif user.quest == 'Продаван':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 3:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 15
                    user.questStatus = 0
                    user.slava += 2
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Делаешь вклад в рынок. Держи награду\nПолучено 15🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю, что твоё задание - продать в Раскуловой хотя бы три предмета. Ты же продал {}.".format(quest.progress)
            elif user.quest == 'Экспедитор':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 1:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 2
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Делаешь вклад в рынок. Держи награду\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю что тебе нужно сгонять в экспедицию."
            elif user.quest == 'Поставщик роз':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if user.roza >= 25:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.roza -= 25
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 2
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Благодаря тебе у меня сегодня будет сэээээкс, гыгыгыгыгы..... Кхм! Прости. Спасибо!\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю что тебе нужно принести мне 25 🌹Роз."
            elif user.quest == 'Поставщик одуванчиков':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if user.oduvanchik >= 25:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 2
                    user.oduvanchik -= 25
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Если что-то годное получится, я тебе сообщу!\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю что я попросил принести мне 25 🌼Одуванчиков."
            elif user.quest == 'Поставщик костей':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                ostanki = await db.Inventory.filter(name='Останки героев', idplayer=user.id, active=1).count()
                if ostanki >= 10:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 2
                    user.dailyBP = 1
                    await db.Inventory.filter(name='Останки геров', idplayer=user.id, active=1).limit(10).delete()
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Если что-то годное получится, я тебе сообщу!\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю что я попросил принести мне 10 🦴Костей."
            elif user.quest == 'Уровнеподъёмщик':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 1:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 15
                    user.questStatus = 0
                    user.slava += 4
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Сегодня точно твой день!\nПолучено 15🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю что я попросил поднять уровень."
            elif user.quest == 'Пряточка':
                quest = await db.tempQuest.get(user_id=user.user_id, quest=user.quest, status=0).first()
                if quest.progress >= 1:
                    quest.timeEnd = time.time() + 86400
                    quest.status = 1
                    user.coupon += 10
                    user.questStatus = 0
                    user.slava += 1
                    user.dailyBP = 1
                    await user.save()
                    await quest.save()
                    await db.tempQuest.filter(user_id=user.user_id, quest=user.quest, status=0).update(status=1)
                    await achprog(user, ach='quest')
                    awardText = await getAwardBp(user)
                    text = "Отлично, красавчик! Сегодня точно твой день!\nПолучено 10🏷\n\n{}".format(awardText)
                else:
                    status = 1
                    text = "Что? Ты еще не закончил же. А, или ты просто поболтать пришёл?\nЕсли вдруг ты перепил, напоминаю что я попросил сыграть в прятки в доме Адского."
        else:
            text = "У тебя ведь есть уже задание, выполни сначала его! \n\n''{}''".format(user.quest)
            status = 1
    else:
        text = "Проваливай отсюда, тебе сюда нельзя!"
        status = 1
    return text, status












#СМЕНА ЗАДАНИЯ

async def quests_(call, user): 
    if (call.from_user.id == call.message.chat.id):
        pass
    else:
        return
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('Назад', callback_data="nav_bigcity_bar"))
    _kach = call.data.split('_')
    q = _kach[1]
    if q == 'change':
        if user.questStatus == 1 and user.questId != 7:
            if user.money >= 200:
                user.money -= 200
                await db.Users.filter(id=user.id).update(questStatus=0, money=user.money)
                await db.tempQuest.filter(user_id=user.user_id).delete()
                await bot.edit_message_text("Вы отказались от задания", call.message.chat.id, call.message.message_id)
            else:
                await bot.edit_message_text("У вас недостаточно денег", call.message.chat.id, call.message.message_id)
        else:
            await bot.edit_message_text("У вас нет активного задания", call.message.chat.id, call.message.message_id)