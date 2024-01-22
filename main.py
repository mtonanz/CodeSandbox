import os
import discord
import sys, re
from googletrans import Translator, LANGUAGES  #pip install googletrans==3.1.0a0 normal versiyon daha verdi
import random
import datetime
from discord.ext import tasks


import keep_alive
keep_alive.awake('https://ozibot.ozimoa.repl.co', True)


my_secret = os.environ['BotToken']
desttimeg = datetime.datetime.today() - datetime.timedelta(hours=5)
desttimes = datetime.datetime.today() - datetime.timedelta(hours=4)
orttime = datetime.datetime.today() - datetime.timedelta(minutes=40)
aztime = datetime.datetime.today() - datetime.timedelta(hours=5)
hocatime = datetime.datetime.today() - datetime.timedelta(minutes=40)
now = datetime.datetime.now()
cnt = 0
sktrcnt = 0
srfsz = [0, 0, 0]
srfszbool = True
pirswitch = False
toplam = 0
upEz = False
upBur = False

bot = discord.Client(intents=discord.Intents.all())
counter = 0


@tasks.loop(seconds=10)
async def my_task(self):
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="HP"))

#Bot kontrol
@bot.event
async def on_ready():
  print('calısıyor')


#chat etkileşimi burada


@bot.event
async def on_message(message):
  #    print(message.author, message.content, message.cnannel.id)   #kontrol satırı gerektiğinde aç

  #burada geri dönüş alınmayacak hesaplar bulunuyor.
  global desttimeg
  global desttimes
  global orttime
  global hocatime
  global aztime
  global now
  global cnt
  global sktrcnt
  global pirswitch
  global toplam
  global upBur
  global upEz
  global srfsz
  global srfszbool

  hocalist = [
      'https://tenor.com/view/adnan-dance-nod-dancing-sexy-dance-gif-17020202',
      'https://tenor.com/view/adnan-gif-24889958',
      'https://tenor.com/view/adnan-oktar-gif-20882481',
      'https://tenor.com/view/adnanoktar-gif-23766797',
      'https://tenor.com/view/olaf-gif-25009371',
      'https://tenor.com/view/adnan-oktar-gif-23766780'
  ]

  if message.author == bot.user:
    if message.content == '<:gulucuk:959973232012853319>':
      desttimeg = now + datetime.timedelta(minutes=10)
      return
    elif message.content == '<:neee:1076615960947069009>':
      desttimes = now + datetime.timedelta(minutes=10)
      return
    elif message.content == 'yalnız o foto öyle atılmaz tek seferlik yollayacaktın!':
      orttime = now + datetime.timedelta(hours=720)
      return
    elif message.content in hocalist:
      hocatime = now + datetime.timedelta(hours=1)
      return
    elif message.content in 'Bana mı seslendiniz ?':
      aztime = now + datetime.timedelta(minutes=20)
    else:
      return

  if 'BotSever' in [
      role.name for role in message.author.roles
  ] or 'Botlar' in [role.name for role in message.author.roles]:
    return

  #çakma komut satırları daha sonra command ile tekrar düzenlenir.
  if '!yak' in message.content.lower():
    await message.channel.send('Yanmayı sizden öğrenecek değiliz!')

  if '!böl' in message.content.lower():
    await message.channel.send('orda duracaksın işte! o ortonun işi.')

  if '!ban' in message.content.lower():
    await message.channel.send(
        'ipek? bırak konuşsun çocuklar sonra gönderirsin silivriye.')

  if ':newsco10:' in message.content.lower():
    await message.channel.send('Güzel şaka Clap Clap')

  if '!deliklitaş' in message.content.lower():
    dlk = discord.Embed()
    dlk.set_image(
        url=
        'https://cdn.discordapp.com/attachments/1058075972135563327/1155412256046194748/IMG_20230403_121456_Buyuk.jpg'
    )
    await message.channel.send('Ozi: ilk penetre olduğum şeydir!', embed=dlk)

  if 'rezillink' in message.content.lower():
    await message.reply('https://hakkarim.net/')

  if '!labadum' in message.content.lower():
    await message.reply('<:guno:1054698128286158869>')

  # Status değişikliği yapmak için bölge
  if '!sinsi' in message.content:
    await bot.change_presence(status=discord.Status.offline)

  if '!sinsof' in message.content:
    await bot.change_presence(status=discord.Status.online)


  if '!serefsiZ' in message.content:
    if srfszbool == True:
      srfszbool = False
    else:
      srfszbool = False

  if ':guno:' in message.content or ':guno~1:' in message.content or ':guno~2:' in message.content or 'güno' in message.content or 'günaydın' in message.content:
    shbt = bot.get_channel(1042165244736319598)
    srfszlist = [261334263532748800, 941299242469834782, 1008383764843475017]
    askhe = bot.get_emoji(1160473684826411118)

    if srfszbool == True:
      if message.guild.id == 1153428693834801222:
        if message.author.id in srfszlist and srfsz[0] == 0:
          srfsz[0] = 1
#          await message.channel.send('<:guno:1054698128286158869> <:ahmetkawai:1138374679355207720>')
          await message.add_reaction(askhe)
        elif message.author.id in srfszlist and srfsz[0] == 1:
          srfsz[0] = 0
          await message.add_reaction(askhe)
      elif message.guild.id == 1088566054244073545:
        if message.author.id in srfszlist and srfsz[1] == 0:
          srfsz[1] = 1
#          await message.channel.send('<:guno:1089497822908387338> <:ahmetkawai:1138374679355207720>')
          await message.add_reaction(askhe)
        elif message.author.id in srfszlist and srfsz[1] == 1:
          srfsz[1] = 0
          await message.add_reaction(askhe)
      elif message.guild.id == 957760263661170738:
        if message.author.id in srfszlist and srfsz[2] == 0:
          srfsz[2] = 1
#          await message.channel.send('<:guno:1054698128286158869> <:ahmetkawai:1138374679355207720>')
          await message.add_reaction(askhe)
        elif message.author.id in srfszlist and srfsz[2] == 1:
          srfsz[2] = 0
          await message.add_reaction(askhe)

    if message.channel == shbt:
      cnt += 1
      print(cnt)
    if cnt == 7:
      cnt = 0
      await shbt.send('<:guno:1054698128286158869>')  # type: ignore

  pat = r'\b[İi]g\b'
  if re.search(
      pat, message.content.lower()) or 'iyi geceler' in message.content.lower(
      ) or 'İyi geceler' in message.content:

    igrand = random.random()
    if igrand >= 0.75:
      await message.reply('skktr skktr bye bye')

  mslmn = r'\bsa\b'
  if re.search(
      mslmn,
      message.content.lower()) or 'selamın aleyküm' in message.content.lower(
      ) or 'selamınaleyküm' in message.content.lower():
    await message.channel.send('Cami mi lan bura? hadi başka kapıya yallah!')

  medet = r'\bhü(ü*)*[gğ]*?$'
  if re.search(medet, message.content.lower()):
    await message.channel.send('HÜ HÜ HÜ Medet Ya ALİİ..')

  if 'kocam' in message.content.lower(
  ) and message.author.id == 663030864103604224:
    buraklist = [
        '<:ooooowww:1153435586527510549>', '<:BurakSleep:1100173847518527491>',
        '<:BurakKiss:1161207016610603018>', '<:BurakSad:1161207023824810054>',
        '<:Burak7:1161207030145617951>',
'<:BurakKesk:1171537416352440341>'
    ]
    randbur = random.choice(buraklist)
    await message.reply(randbur)

  if '!sıfırla' in message.content.lower():
    desttimes = now
    desttimeg = now
    orttime = now
    hocatime = now
    aztime = now

    await message.channel.send('pkibbcm?')

  if 'daha uzun' in message.content.lower():
    await message.channel.send(
        '<:otter3:1115341549568532530><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter2:1115341545856577656><:otter1:1115341542861848637>'
    )

  if '!holter' in message.content.lower():
    buyuk = random.randint(120, 200)
    kucuk = buyuk - random.randint(40, 70)
    nabiz = random.randint(85, 175)
    ezrand = random.random()
    if ezrand < 0.1:
      await message.channel.send(f'<@1008383764843475017>')
    else:
      await message.channel.send(f'{buyuk}/{kucuk}-{nabiz}')

  if 'genel' in message.content.lower():
    nani = bot.get_emoji(976071072300539904)
    await message.add_reaction(nani)

  if '!pati' in message.content.lower():
    await message.reply('<:oziPati:1088217962235822160>')

  hocoff = True
  if hocoff == False and 'hocam' in message.content.lower():
    if hocatime > datetime.datetime.now():
      return
    else:
      pick = random.choice(hocalist)
      await message.channel.send(pick)

  if 'Azer' in message.content or 'AzerKaçak' in message.content:
    if aztime > now:
      return
    else:
      await message.channel.send('Bana mı seslendiniz ?')

  if '!ilan' in message.content.lower():
    azlist = [
        'Hamma Salam Qadını Dilimlə Boşaldıram Və Masaj Edirəm. Bütün Xidmətlər Pulsuzdur. Reel İstəyən Qadinlar Whatsapp-Da Əlavə Edə Bilər. Heç Qadin Qorxu Olmayacaq, Xeyt',
        'Amcıx Və Göt Əmirəm Yalıyıram, İsdəsəniz Ağzıma Boşalın Və Ağzıma İşiyin. İsdəyən Xanımlar Yazsın'
    ]
    await message.channel.send(random.choice(azlist))

  #gulucukserisi
  if '🙂' in message.content.lower() or ':gulucuk:' in message.content.lower(
  ) or ':twitchsmile:' in message.content.lower():
    if desttimeg > now:
      return
    else:
      await message.channel.send('<:gulucuk:959973232012853319>')

  #sasırmaserisi
  if ':DD:' in message.content or ':neh:' in message.content or 'D:' in message.content:

    if desttimes > now:
      return
    else:
      await message.channel.send('<:neee:1076615960947069009>')

  if 'yak yak yak' in message.content.lower():
    await message.channel.send('söndür onu hemen bak aleviler var aramızda!')

  image_format = ['.jpeg', '.jpg', '.png', '.dng']
  if len(message.attachments) > 0:
    attachment = message.attachments[0]
    for i in image_format:
      if i in attachment.filename and 'SPOILER_' in attachment.filename:
        await message.reply('Nude mu lan o?')

    orto = await bot.fetch_user(261334263532748800)
    if message.author == orto:
      for i in image_format:
        if i in attachment.filename:
          if orttime > now:
            return
          else:
            await message.reply(
                'yalnız o foto öyle atılmaz tek seferlik yollayacaktın!')

  sibel = bot.get_emoji(1051857342616043552)
  mkp = bot.get_emoji(1074044827831910511)

  if '!sibel' in message.content.lower():
    sibembed = discord.Embed()
    sibembed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/1058075972135563327/1063613532807106560/Ekran_goruntusu_2023-01-14_031959.png'
    )
    await message.channel.send(f'{sibel}', embed=sibembed)

  if 'vajinismus' in message.content.lower():
    await message.channel.send(f'{mkp}')

  if 'ay ay ay' in message.content.lower():
    await message.channel.send('AY AY AY AY AY AŞU be!')

  if '$abdullahgül' in message.content.lower():
    await message.channel.send('Artık herkes evine dönmeli!')
    sys.exit('komut ile sonlandırıldı')

  #genel çeviri kısmı burada
  lang = 'ku'  # 'az'
  Ruya = bot.get_channel(1079905237000785940)
  langlist = LANGUAGES
  global counter
  ranlim = 3
  person = r"<@*[0-9]+>"

  if '!hipnoz' in message.content.lower():
    cevirici = Translator(service_urls=['translate.googleapis.com'])
    hpn = 'SEKSİN SONU OLUR HİPNOZUN SONU OLMAZ'
    keys = list(langlist.keys())
    lang = random.choice(keys)
    htrns = cevirici.translate(hpn, dest=lang)
    await message.channel.send(yolla(htrns))

#trol ne-yapay zeka

  tsoh = bot.get_channel(1089488593069809765)
  sohbet = bot.get_channel(1153428695520903321)
  tses = bot.get_channel(1089488730835931197)
  teras = bot.get_channel(1153428695520903322)
  forum = bot.get_channel(1092410640980774953)
  cevirici = Translator(service_urls=['translate.googleapis.com'])
  if message.channel == tsoh:
    gond = message.content
    await sohbet.send(gond)  # type: ignore
  if message.channel == tses:
    gond = message.content
    await teras.send(gond)  # type: ignore

  numb = message.content.count(':')
  if numb < 9:
    emjchck = True
  else:
    emjchck = False

  transfoff = True

  if transfoff == False and len(message.content) >= 180 and (
      message.channel != Ruya
      or message.channel != forum) and len(message.content) < 2000 and emjchck:
    cevirici = Translator(service_urls=['translate.googleapis.com'])
    try:
      if counter == ranlim:
        keys = list(langlist.keys())
        lang = random.choice(keys)
        if lang == 'tr' or lang == 'az':
          lang = random.choice(keys)
        print(langlist[lang], lang)
        counter = 0
      msg = re.sub(person, '', message.content)
      if '@' in msg:
        msg = msg.replace('@', '')

      cevrilmis = cevirici.translate(msg, dest=lang)
      azce = cevirici.translate(msg, dest='az')
      cevrilmis = yolla(cevrilmis)
      azce = yolla(azce)

      if message.content != cevrilmis:
        await message.channel.send(
            f'{azce} \n----------------------- \n{cevrilmis}')
        counter += 1

    except AttributeError:
      print('cevrilemedi')


#elif kısmı talihsiz açıklamaları kapsıyor
  guilds = [
      957760263661170738, 947897025305927691, 1088566054244073545,
      1153428693834801222
  ]
  talihsizler = [
      959167545468936222, 1076810424042926131, 1088566572983001088,
      1153441713940070461
  ]
  teesüfediciler = [
      1062290362716139530, 1076810448814485555, 1088605101293314138,
      1153441758747840512
  ]

  i = guilds.index(message.guild.id)
  talihsiz = bot.get_channel(talihsizler[i])
  teesüfedici = bot.get_channel(teesüfediciler[i])

  if message.channel == talihsiz:
    cevirici = Translator(service_urls=['translate.googleapis.com'])
    try:
      if counter == ranlim:
        keys = list(langlist.keys())
        lang = random.choice(keys)
        if lang == 'tr' or lang == 'az':
          lang = random.choice(keys)
        print(langlist[lang], lang)
        counter = 0

      msg = re.sub(person, '', message.content)
      if '@' in msg:
        msg = msg.replace('@', '')

      try:
        mesaj, soyleyen = msg.split('-')
        cevrilmis = cevirici.translate(mesaj, dest=lang)
        azce = cevirici.translate(mesaj, dest='az')
        cevrilmis = yolla(cevrilmis) + ' -' + soyleyen
        azce = yolla(azce) + ' -' + soyleyen
      except:
        cevrilmis = cevirici.translate(msg, dest=lang)
        azce = cevirici.translate(msg, dest='az')
        cevrilmis = yolla(cevrilmis)
        azce = yolla(cevrilmis)

      if message.content != cevrilmis:
        await teesüfedici.send(
            f'{azce} \n----------------------- \n{cevrilmis}')  # type: ignore
        counter += 1

    except AttributeError:
      print('cevrilemedi')

  if '!piraç' in message.content.lower():
    pirswitch = True
  if '!pirkapa' in message.content.lower():
    pirswitch = False
  PPattern = r'\bbir\w{0,}\b'

  if pirswitch and message.channel == teras:
    if re.search(PPattern, message.content):
      Pirtext = re.sub(PPattern,
                       lambda match: match.group(0).replace('bir', 'pir'),
                       message.content.lower())
      await message.channel.send(f'{Pirtext}')


  #sesliye gelene tepki vermek
@bot.event
async def on_voice_state_update(member, before, after):
  global now
  kullanicilist = {
      261334263532748800: 'Harun',
      941299242469834782: 'Haruncuk',
      555116701822484481: 'Ozi',
      155777897854926848: 'Burak',
      750107488480788543: 'Burak gelmişken kamera da aç',
      663030864103604224: 'Bilge',
      808038686452744192: 'Tarık',
      412347553141751808: 'Sakin olun müzik çalıp gidecek',
      1041372741661622414: 'Tarık',
      342798286090141697: 'Mambik',
      689894639448227869: 'Kürdün Hası',
      377172951256137729: 'Berkay',
      371765589330624512: 'Miğfer',
      395268362504110081: 'Berk',
      696057540580081674: 'İpek',
      568911931147026444: 'Ay Ay Ay Aşu',
      1008383764843475017: 'Ezgim',
      694936695128457368: 'Modların Kraliçesi',
      708386975182225489: 'Imss velo',
      412347257233604609: 'Sakin olun müzik falan işleri var bunun'
  }  # Bunlar Eklenecek

  if not before.channel and after.channel and member.id == 1008383764843475017:
    iltifat = [
        'Bakarsa bakar mısın?',
        'Ortomda bir ağırlık var. aaa taş gibi bir bey gelmiş.',
        'e e e ezgiiieeehh', 'Ankara şimdi daha güzel.', 'Öhöööööömmm!',
        'Haaaaruuunn bak', 'Zaman pamuk gibi olma zamanı'
    ]  #Bura Düzenlenecek
    bu = random.choice(iltifat)
    saat = int(now.hour)
    if 18 <= saat and saat < 23:
      await after.channel.send(
          f'{bu} ' + ' güneş yeniden doğmuş <:gulucuk:959973232012853319>'
      )  # type: ignore
    if 0 <= saat and saat < 8:
      await after.channel.send(
          f'{bu} ' + '<:gulucuk:959973232012853319> Geceme gün doğdu.'
      )  # type: ignore
    if 8 <= saat and saat < 18:
      await after.channel.send(
          f'{bu} ' +
          'Güneş bu güzelliği kıskanır be! <:gulucuk:959973232012853319>'
      )  # type: ignore

  if not before.channel and after.channel:
    if member.id in kullanicilist:
      await after.channel.send(f'Xoş gəldin {kullanicilist[member.id]}')
    else:
      await after.channel.send(f'Xoş geldin {member.nick}')

  if before.channel and not after.channel:
    if member.id == 412347553141751808:
      await before.channel.send(f'Amaaan bu da çok bayık hemen gidiyor.')
    if member.id in kullanicilist:
      await before.channel.send(
          f'sktrr orospu, hadi gülügülü {kullanicilist[member.id]} gülügülü ')


def yolla(bunu):
  return (bunu.text)




bot.run(my_secret)
