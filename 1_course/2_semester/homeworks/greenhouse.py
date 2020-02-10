import time, threading


class Greenhouse():
    __windows = [False, False]
    __opened_windows = 0
    __heaters = [False, False, False]
    __working_heaters = 0
    __fuse = False
    __humidity = 36.2
    __temperature = 10
    __start_time = 0
    __thread_active = True

    def __init__(self):
        self.__start_time = time.time()
        self.__thread = threading.Thread(target=self.__change)
        self.__thread.start()

    def __change(self):
        while True and self.__thread_active:
            current_time = time.time()
            if current_time - self.__start_time > 5:
                if self.__humidity > 65:
                    self.__temperature = self.__temperature - 1.4 - self.__opened_windows * 0.9 + self.__working_heaters * 2.3
                else:
                    self.__temperature = self.__temperature - 2.4 - self.__opened_windows * 1.4 + self.__working_heaters * 1.5 + self.__humidity * 0.012

                if self.__temperature > 16:
                    self.__humidity += 4.6 * (self.__opened_windows - self.__working_heaters) ** 2
                else:
                    self.__humidity -= (self.__opened_windows - self.__working_heaters) * 3.8

                self.__check_conditions()
                self.__start_time = current_time
            time.sleep(0.1)

    def __check_conditions(self):
        if self.__temperature > (30.5 - self.__humidity * 0.013) or self.__temperature < 0 or self.__humidity < 9.5 or self.__humidity > 91.2:
            self.__deactivate()

    def __deactivate(self):
        self.__fuse = True
        for i in range(2):
            self.__windows[i] = True
        for i in range(3):
            self.__heaters[i] = False

    def __check_state(self):
        if self.__fuse:
            return False, 'You cannot change any conditions, because the greenhouse is working in in emergency mode'
        else:
            return True, ''

    def open_window(self) -> (bool, str):
        success, res = self.__check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All windows are opened'
        if self.__opened_windows != 2:
            i = 0
            while self.__windows[i]:
                i += 1
            self.__windows[i] = True
            self.__opened_windows += 1
            success = True
            res = "One of the windows was opened"
        return success, res

    def close_window(self) -> (bool, str):
        success, res = self.__check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All windows are closed'
        if self.__opened_windows != 0:
            i = 0
            while not self.__windows[i]:
                i += 1
            self.__windows[i] = False
            self.__opened_windows -= 1
            success = True
            res = 'Window was closed'
        return success, res

    def switch_on_heater(self) -> (bool, str):
        success, res = self.__check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All heaters are working'
        if self.__working_heaters != 3:
            i = 0
            while self.__heaters[i]:
                i += 1
            self.__heaters[i] = True
            self.__working_heaters += 1
            success = True
            res = "One of the heaters was turned on"
        return success, res

    def switch_off_heater(self) -> (bool, str):
        success, res = self.__check_state()
        if not success:
            return success, res

        success = False
        res = 'Failure. All heaters aren\'t working\n'
        if self.__working_heaters != 0:
            i = 0
            while not self.__heaters[i]:
                i += 1
            self.__heaters[i] = False
            self.__working_heaters += 1
            success = True
            res = "One of the heaters was turned off"
        return success, res

    def stop(self):
        self.__thread_active = False

    def passed_time(self):
        current_time = time.time()
        passed = int(current_time - self.__start_time)
        return True, f'{passed} sec passed'

    def __str__(self):
        if self.__fuse:
            return 'Greenhouse broke down'
        else:
            return f'The greenhouse works properly. \n' \
                   f'There are: {len(self.__windows)} windows ({self.__opened_windows} opened); ' \
                   f'{len(self.__heaters)} heaters ({self.__working_heaters} working).\n' \
                   f'Temperature: {self.__temperature} C; humidity: {self.__humidity} % \n'
