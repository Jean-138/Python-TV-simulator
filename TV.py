

class Television:
    def __init__(self):
        self.channel = 1
        self.volume = 30
        self.max_volume = 100
        self.min_volume = 1
        self.max_channel = 99
        self.min_channel = 1
        self.is_on = False
        self.muted_volume = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def channel_up(self):
        if not self.is_on:
            return

        if self.channel < self.max_channel:
            self.channel += 1

    def channel_down(self):
        if not self.is_on:
            return

        if self.channel > self.min_channel:
            self.channel -= 1

    def increase_volume(self):
        if not self.is_on:
            return

        if self.volume < self.max_volume:
            self.volume += 1

    def decrease_volume(self):
        if not self.is_on:
            return

        if self.volume > self.min_volume:
            self.volume -= 1

    def mute(self):
        if not self.is_on:
            return

        self.muted_volume = self.volume
        self.volume = 0
        print("The TV is muted")

    def unmute(self):
        if not self.is_on:
            return

        if self.muted_volume is not None:
            self.volume = self.muted_volume
            self.muted_volume = None
            print("The TV is unmuted and volume restored to", self.volume)
        else:
            print("The TV is not muted")

    def __str__(self) -> str:
        return f"Television - Is on: {self.is_on} - Channel: {self.channel} - Volume: {self.volume}"


# Test section
tv_test = Television()

print("Is the TV on?", tv_test.is_on)

tv_test.turn_on()
print("Is the TV on now?", tv_test.is_on)

tv_test.turn_off()
print("Is the TV on now?", tv_test.is_on)

tv_test.turn_on()
print("Is the TV on now?", tv_test.is_on)

print("Current channel:", tv_test.channel)

tv_test.channel_up()
print("New channel:", tv_test.channel)

tv_test.channel_down()
print("New channel:", tv_test.channel)

print("Initial volume:", tv_test.volume)

tv_test.increase_volume()
print("Volume is now:", tv_test.volume)

tv_test.decrease_volume()
tv_test.decrease_volume()
print("New volume:", tv_test.volume)

tv_test.mute()
tv_test.unmute()
