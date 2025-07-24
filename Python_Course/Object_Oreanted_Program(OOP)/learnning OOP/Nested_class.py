from typing import Optional
from abc import ABC, abstractmethod

class Device(ABC):
    totol_no_of_device = 0
    device = list()
    
    def __init__(self) -> None:
        Device.totol_no_of_device += 1
        self.device_id = Device.totol_no_of_device
    def show_total_no_of_device(self):
        return Device.totol_no_of_device
        
class Laptop(Device):
    total_no_of_laptop = 0
    class Battery:
        def __init__(self, battery) -> None:
            self.battery = battery

        def show_battery_detail(self):
            return str(self.battery) + "V"
    class GPU:

        def __init__(self, gpu) -> None:
            # if gpu is None:
            #     self.gpu = None
            # else:
            #     self.gpu = gpu
            self.gpu = gpu or None

        def show_gpu_detail(self):
            return self.gpu
    class Screen_touch:
        def __init__(self, is_screen_touch) -> None:
            self.is_screen_touch = is_screen_touch
    
        def show_is_screen_touch_detail(self):
            return self.is_screen_touch
    class Display:
        def __init__(self, display) -> None:
            self.display = display

        def show_display_detail(self):
            return self.display
   
    def __init__(self, name : str, price : int, battery : int, display : str, is_screen_touch : bool, brand : str, gpu : Optional[str] = None) -> None:
        self.name = name.capitalize()
        self.price = price
        self.brand = brand
        self.battery = self.Battery(battery)
        self.gpu = self.GPU(gpu)
        self.display = self.Display(display)
        self.is_screen_touch = self.Screen_touch(is_screen_touch)

        Laptop.total_no_of_laptop += 1
        self.id = Laptop.total_no_of_laptop
        super().__init__()   
    def __str__(self) -> str:
        return f"{self.id}{self.name}, {self.price}, {self.battery.show_battery_detail()}, {self.gpu.show_gpu_detail()}, {self.display.show_display_detail()}, {self.is_screen_touch.show_is_screen_touch_detail()}"
class Computer(Device):
    total_no_of_computer = 0
    class Battery:
        def __init__(self, battery) -> None:
            self.battery = battery

        def show_battery_detail(self):
            return str(self.battery) + "V"
    class GPU:
        def __init__(self, gpu) -> None:
            self.gpu = gpu or None

        def show_gpu_detail(self):
            return self.gpu
    class Screen_touch:
        def __init__(self, is_screen_touch) -> None:
            self.is_screen_touch = is_screen_touch

        def show_is_screen_touch_detail(self):
            return self.is_screen_touch
    class Display:
        def __init__(self, display) -> None:
            self.display = display

        def show_display_detail(self):
            return self.display

    def __init__(self, name : str, price : int, battery : int, display : str, is_screen_touch : bool, brand : str, gpu : Optional[str] = None) -> None:
        self.name = name.capitalize()
        self.price = price
        self.brand = brand
        self.battery = self.Battery(battery)
        self.gpu = self.GPU(gpu)
        self.display = self.Display(display)
        self.is_screen_touch = self.Screen_touch(is_screen_touch)

        Computer.total_no_of_computer += 1
        self.id = Computer.total_no_of_computer
        super().__init__()
    def __str__(self) -> str:
        return f"{self.id}{self.name}, {self.price}, {self.battery.show_battery_detail()}, {self.gpu.show_gpu_detail()}, {self.display.show_display_detail()}, {self.is_screen_touch.show_is_screen_touch_detail()}"


class Showroom(ABC):
    no_of_showroom = 0
    showrooms = list()
    def __init__(self, name) -> None:
        self.name = name
        Showroom.no_of_showroom += 1
        self.add_showroom(name)
        
    def add_showroom(self, name) -> None:
        Showroom.showrooms.append(name)
    def show_showroom(self):
        return Showroom.showrooms
    
class Apple_showroom(Showroom):
    no_of_Apple_showroom = 0
    def __init__(self, name) -> None:
        super().__init__(name)
        Apple_showroom.no_of_Apple_showroom += 1
        
class Other_showroom(Showroom):
    no_of_other_showroom = 0
    def __init__(self, name) -> None:
        super().__init__(name)
        Other_showroom.no_of_other_showroom += 1

apple_showroom1 = Apple_showroom(name = "ankit_apple1")
apple_showroom2 = Apple_showroom(name = "ankit_apple2")
other_showroom1 = Other_showroom(name = "ankit_other1")
other_showroom2 = Other_showroom(name = "ankit_other2")


