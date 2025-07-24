from typing import Optional
from abc import ABC, abstractmethod

class Device(ABC):
    totol_no_of_device = 0
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
   
    def __init__(self, name : str, price : int, battery : int, display : str, is_screen_touch : bool, gpu : Optional[str] = None) -> None:
        self.name = name.capitalize()
        self.price = price
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

    def __init__(self, name : str, price : int, battery : int, display : str, is_screen_touch : bool, gpu : Optional[str] = None) -> None:
        self.name = name.capitalize()
        self.price = price
        self.battery = self.Battery(battery)
        self.gpu = self.GPU(gpu)
        self.display = self.Display(display)
        self.is_screen_touch = self.Screen_touch(is_screen_touch)

        Computer.total_no_of_computer += 1
        self.id = Computer.total_no_of_computer
        super().__init__()


    def __str__(self) -> str:
        return f"{self.id}{self.name}, {self.price}, {self.battery.show_battery_detail()}, {self.gpu.show_gpu_detail()}, {self.display.show_display_detail()}, {self.is_screen_touch.show_is_screen_touch_detail()}"

laptop1 = Laptop(name = "lenovo slim pro", price = 1000, battery = 5, display= "Multi-Color", is_screen_touch= True)
laptop2 = Laptop(name = "lenovo slim pro", price = 1000, battery = 5, display= "Multi-Color", is_screen_touch= True)
laptop3 = Laptop(name = "lenovo slim pro", price = 1000, battery = 5, display= "Multi-Color", is_screen_touch= True)
compter1 = Computer(name = "lenovo slim pro", price = 1000, battery = 5, display= "Multi-Color", is_screen_touch= True)
compter2 = Computer(name = "lenovo slim pro", price = 1000, battery = 5, display= "Multi-Color", is_screen_touch= True)


# print(laptop1.id)
# print(laptop1.name)
# print(laptop1.price)
# print(laptop1.battery.show_battery_detail())
# print(laptop1.gpu.show_gpu_detail())
# print(laptop1.display.show_display_detail())
# print(laptop1.is_screen_touch.show_is_screen_touch_detail())
# print(compter2.device_id)

print(Laptop.total_no_of_laptop)
print(Computer.total_no_of_computer)
print(Device.totol_no_of_device)

