class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"

class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"

# 3 Гибриддик мурас
class GlowStreamer(Streamer,Mutant):
    def ultimate_content(self):
        x = self.earn()
        y = self.superpower()
        return f"{x} + {y}"

class ViralCyborg(TikToker,Mutant):
    def ultimate_content(self):
        x = self.live()
        y = self.superpower()
        return f"{x} + {y}"

class DonateMage(Streamer,TikToker):
     def ultimate_content(self):
         x = self.earn()
         y = self.viral()
         return f"{x} + {y}"

glow_streamer = GlowStreamer()
viral_cyborg = ViralCyborg()
donate_mage = DonateMage()

print(f"__mro__ :CHARACTERS: ")
print(GlowStreamer.__mro__)
print(ViralCyborg.__mro__)
print(DonateMage.__mro__)
print(f"live() FOR EVERY OBJECTS:")
print(glow_streamer.live())
print(viral_cyborg.live())
print(donate_mage.live())
print(f"ultimate_content() FOR EVERY OBJECTS:")
print(glow_streamer.ultimate_content())
print(viral_cyborg.ultimate_content())
print(donate_mage.ultimate_content())
