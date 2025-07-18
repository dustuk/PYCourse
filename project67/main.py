import csv
import os
os.chdir(r"C:\Users\iejhd\Desktop\programs\PY\PYCourse\project67")

class Employee:
    #--------------- Class Attributes -------------------
    company = "Alawjan"
    PHONE_PREFIX = "+20"
    PHONE_LENGTH = 12
    
    #--------------- Constructor -------------------
    def __init__(self, name: str, age: str, job: str, id: str, phone: str, bank_account: str, 
    hours_worked: float=160, hourly_rate: float=15, from_file: bool=False) -> None:
        self.name = name
        self.age = age
        self.job = job
        self.__id = id
        self.__phone = phone
        self.__bank_account = bank_account
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate
        if not from_file:
            AllEmployees.add_employee(self)
    
    #--------------- Setters and Getters -------------------
    @property
    def id(self) -> str:
        return self.__id
    
    # يتحقق من صحة معرف الموظف (يجب أن يكون نصًا غير فارغ مكوّنًا من أرقام فقط)
    @id.setter
    def id(self, id: str) -> None:
        if isinstance(id, str) and id.isdigit() and id.strip():
            self.__id = id
        else:
            raise ValueError("ID should be non-empty string composed only of digits")
    
    @property
    def phone(self) -> str:
        return self.__phone
    
    # يتحقق من صحة رقم الهاتف بناءً على معيار الشركة (+20 وطول 12 رقم)
    @phone.setter
    def phone(self, phone: str) -> None:
        if Employee.is_valid_phone(phone):
            self.__phone = phone
        else:
            raise ValueError("Phone number should start with +20 and be 12 digits long")
    
    @property
    def hours_worked(self) -> float:
        return self.__hours_worked
    
    # يتأكد من أن ساعات العمل إيجابية وصحيحة (عدد صحيح أو عشري)
    @hours_worked.setter
    def hours_worked(self, new_hours: float) -> None:
        if isinstance(new_hours, (int, float)) and new_hours > 0:
            self.__hours_worked = new_hours
        else:
            raise ValueError("Hours worked must be a positive number")
    
    @property
    def hourly_rate(self) -> float:
        return self.__hourly_rate
    
    # يتأكد من أن الأجر بالساعة إيجابي وصحيح (عدد صحيح أو عشري)
    @hourly_rate.setter
    def hourly_rate(self, new_rate: float) -> None:
        if isinstance(new_rate, (int, float)) and new_rate > 0:
            self.__hourly_rate = new_rate
        else:
            raise ValueError("Hourly rate must be a positive number")
    
    #--------------- Instance Methods -------------------
    # يحسب الراتب الإجمالي بضرب ساعات العمل في الأجر بالساعة
    def calculate_gross_salary(self) -> float:
        return self.__hours_worked * self.__hourly_rate
    
    # يحسب الراتب الصافي بعد خصم الضرائب والتأمين والتقاعد
    def calculate_net_salary(self) -> float:
        gross_salary = self.calculate_gross_salary()
        return Finance.calculate_net_salary(gross_salary)
    
    # تحديث ساعات العمل والأجر مع التحقق من صحة القيم
    def update_work_details(self, new_hours: float, new_rate: float) -> None:
        self.hours_worked = new_hours
        self.hourly_rate = new_rate

    #--------------- Static Methods -------------------
    # يتحقق من صحة رقم الهاتف حسب قواعد الشركة
    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        return phone.startswith(Employee.PHONE_PREFIX) and len(phone) == Employee.PHONE_LENGTH
    
    #--------------- Magic Methods -------------------
    # تمثيل نصي بسيط للموظف للمستخدم
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old and works as {self.job} and his id is {self.__id} and his phone number is {self.__phone} and his bank account is {self.__bank_account}"
    
    # تمثيل نصي للموظف للمطور (تفصيلي)
    def __repr__(self) -> str:
        return f"Employee name = {self.name}, age = {self.age}, job = {self.job}, id = {self.__id}, phone = {self.__phone}, bank_account = {self.__bank_account}"

class Manger(Employee):
    #--------------- Class Attributes -------------------
    MANAGER_BONUS = 500
    
    #--------------- Constructor -------------------
    def __init__(self, *args, authority_level: int=1, **kwargs) -> None:
        # تطبيق مبدأ الوراثة
        super().__init__(*args, **kwargs)
        self.authority_level = authority_level
    
    #--------------- Instance Methods -------------------
    def calculate_gross_salary(self):
        return super().calculate_gross_salary() + self.MANAGER_BONUS
    
    # ترقية للموظف وزيادة الراتب بناء على المعرف
    def promote_employee(self, employee_id: str, raise_amount: float) -> None:
        if raise_amount > 0:
            employee = AllEmployees.get_employee_by_id(employee_id)
            new_rate = employee.hourly_rate + raise_amount
            employee.hourly_rate = new_rate
        else:
            raise ValueError("Raise amount must be a positive number")  
        
    # تنزيل للموظف وتقليل الراتب بناء على المعرف بشرط ان مستوى المدير اكبر او يساوي 2
    def demote_employee(self, employee_id: str, raise_amount: float) -> None:
        if self.authority_level >= 2:
            if raise_amount > 0:
                employee = AllEmployees.get_employee_by_id(employee_id)
                # max يمنع الراتب ان يكون اقل من 3
                new_rate = max(employee.hourly_rate - raise_amount, 3)
                employee.hourly_rate = new_rate
            else:
                raise ValueError("Raise amount must be a positive number")
        else:
            # يعطي خطأ اذا كان مستوى المدير اقل من 2
            raise PermissionError("You don't have permission to demote employees")

    # طرد الموظف بناء على المعرف وبشرط ان مستوى المدير اكبر او يساوي 3
    def fire_employee(self, employee_id: str) -> None:
        if self.authority_level >= 3:
            AllEmployees.remove_employee_by_id(employee_id)
        else:
            # يعطي خطاء اذا كان مستوى المدير اقل من 3
            raise PermissionError("You don't have permission to fire employees")
    
    #--------------- Magic Methods -------------------
    def __str__(self) -> str:
        return f"{super().__str__()} and his authority level is {self.authority_level}"
        
class EmployeeFileHandler:
    #--------------- Static Methods -------------------
    # قراءة بيانات الموظفين من ملف CSV وتحويلها لكائنات Employee
    @staticmethod
    def read_csv_data(file_path: str) -> list:
        employees = []
        with open(file_path, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                name = row["name"]
                age = row["age"]
                job = row["job_title"] 
                id = row["id"]
                phone = row["phone"]
                bank_account = row["bank_account"]
                hours_worked = float(row["hours_worked"])
                hourly_rate = float(row["hourly_rate"])
                employee = Employee(name, age, job, id, phone, bank_account, hours_worked, hourly_rate, from_file=True)
                employees.append(employee)
        return employees

    # يضيف الموظفين المقروءين إلى قائمة الكل إذا لم يكونوا موجودين مسبقًا
    @staticmethod
    def read_and_add_to_AllEmployees(file_path: str) -> None:
        employees_list = EmployeeFileHandler.read_csv_data(file_path)
        for emp in employees_list:
            AllEmployees.add_employee(emp)
            
class AllEmployees:
    #--------------- Class Attributes -------------------
    __employees = []
    
    #--------------- Class Methods -------------------
    # يضيف موظفًا إلى القائمة إذا لم يكن مكررًا بناءً على المعرف
    @classmethod
    def add_employee(cls, employee: Employee) -> None:
        if employee.id not in [emp.id for emp in cls.__employees]:
            cls.__employees.append(employee)
    
    # يعرض جميع الموظفين
    @classmethod
    def list_all_employees(cls) -> list:
        return cls.__employees
    
    # يبحث عن موظف بناءً على المعرف ويرجعه، أو يرفع خطأ إذا لم يجده
    @classmethod
    def get_employee_by_id(cls, employee_id: str) -> Employee:
        for emp in cls.__employees:
            if emp.id == employee_id:
                return emp
        raise ValueError("Employee not found")
    
    # يحذف موظف من القائمة بناءً على المعرف، أو يرفع خطأ إذا لم يجده
    @classmethod
    def remove_employee_by_id(cls, employee_id: str) -> None:
        cls.get_employee_by_id(employee_id)
        cls.__employees = [emp for emp in cls.__employees if emp.id != employee_id]
        
class Finance:
    #--------------- Class Attributes -------------------
    TAX_THRESHOLD = 5000
    TAX_LOW = 0.1
    TAX_HIGH = 0.3
    HEALTH_INSURANCE_COST = 100
    RETIREMENT_CONTRIBUTION_RATE = 0.05
    
    #--------------- Static Methods -------------------
    # يحسب صافي الراتب بعد خصم الضرائب، التأمين الصحي، ومساهمات التقاعد
    @staticmethod
    def calculate_net_salary(gross_salary: float) -> float:
        tax = Finance.calculate_tax(gross_salary)
        retirement_contribution = gross_salary * Finance.RETIREMENT_CONTRIBUTION_RATE
        total_deductions = tax + Finance.HEALTH_INSURANCE_COST + retirement_contribution
        net_salary = gross_salary - total_deductions
        return net_salary
    
    # يحسب الضريبة حسب قيمة الراتب (10% إذا أقل من العتبة، وإلا 30%)
    @staticmethod
    def calculate_tax(salary: float) -> float:
        return salary * Finance.TAX_LOW if salary < Finance.TAX_THRESHOLD else salary * Finance.TAX_HIGH


EmployeeFileHandler.read_and_add_to_AllEmployees("employees_data.csv")
manger = Manger("elboss", 50, "Manger", "234235", "0123456789", "1234567890", 160, 100, authority_level=3)