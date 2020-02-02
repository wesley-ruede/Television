class Television:

    def __init__(self,power=True):
        self.power = power
        self.channel_list = [-1,0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
        self.current_channel = 1
        self.channel_index = self.channel_list.index(self.current_channel)
        self.current_volume = 5
        self.volume_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.volume_index = self.volume_list.index(self.current_volume)

        self.tv_show = {1:'news',2:'cooking',3:'how to improve your house',4:'music',5:'soap opera',6:'gardening',7:'cartoons',
                         8:'a sci-fi show',9:'travel',10:'sports',11:'religion',12:'porn',13:'more music',14:'food tavel',
                         15:'sales',16:'talk show',17:'comedy',0:'HDMI 1',-1:'HDMI 2',18:'a movie',19:'video game show'}

    def turnOn(self):
        if self.power == False:
            return False
        elif self.power == True:
            return True
        else:
            return 'there is an error in the tv'

    def turnOff(self):
        self.power =  False
        return False

    def chooseChannel(self,channel):
        if Television.turnOn(self) == True: # check if the tv is on
            if channel not in self.channel_list:
                print('choose a channel from the channel list ',self.channel_list)
                try:
                    channel = int(input('enter a channel: '))
                except ValueError as e:
                    print(e)
                Television.chooseChannel(self,channel)
            elif channel in self.channel_list:
                self.channel_index = self.channel_list.index(channel)
                self.current_channel = self.channel_list[self.channel_index]
                channel_to_show = self.tv_show.get(self.current_channel)
                print(f'the channel has been changed to: {channel_to_show}')
                return True
            else:
                print(f'the channel could not be changed to: {self.current_channel}')
                return False
        else:
            print('you need to turn the tv on')
            return None

    def channelUpOrDown(self,up_or_down):
        up = ['up','UP','Up','uP']
        down = ['Down','DOWN','down']
        if self.current_channel is not None:
            if up_or_down in up:
                try:
                    self.channel_index = self.channel_list.index(self.current_channel)
                    self.current_channel = self.channel_list[self.channel_index + 1]
                    channel_to_show = self.tv_show.get(self.current_channel)
                    print(f'The channel went up. You are watching: {channel_to_show}')
                    return True
                except IndexError as e:
                    print(e)
                    print('you are at the last channel, try going down')
            elif up_or_down in down:
                try:
                    self.channel_index = self.channel_list.index(self.current_channel)
                    self.current_channel = self.channel_list[self.channel_index - 1]
                    channel_to_show = self.tv_show.get(self.current_channel)
                    print(f'The channel went down. You are watching: {channel_to_show}')
                    return False
                except IndexError as e:
                    print(e)
                    print('you are at the first channel, try going up')
            else:
                return 'are you sure you put in "up" or "down"'
        else:
            return 'you idn\'t press up or down'

    def volumeUpOrDown(self,up_or_down):
        up = ['up','UP','Up','uP']
        down = ['Down','DOWN','down']
        if self.current_volume is not None:
            if up_or_down in up:
                try:
                    self.volume_index = self.volume_list.index(self.current_volume)
                    self.current_volume = self.volume_list[self.volume_index + 1]
                    print(f'The volume went up. The current volume level is {self.current_volume}')
                    return True
                except IndexError as e:
                    print(e)
                    print('The tv\'s volume is maxed out. It\'s really loud.')
            elif up_or_down in down:
                try:
                    self.volume_index = self.volume_list.index(self.current_volume)
                    # I need to find  way to stop this volume level going below 0.
                    self.current_volume = self.volume_list[self.volume_index - 1] % len(self.volume_list)
                    print(f'The volume went down. The current volume level is {self.current_volume}')
                    return False
                except IndexError as e:
                    print(e)
                    print('The tv is already muted.')
            else:
                return 'are you sure you put in "up" or "down"'
        else:
            return 'you didn\'t press up or down'

tv = Television()
tv.turnOn()
tv.chooseChannel(8)
tv.channelUpOrDown('Up')
tv.channelUpOrDown('Up')
tv.channelUpOrDown('down')
tv.volumeUpOrDown('up')
tv.volumeUpOrDown('Down')
