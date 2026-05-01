#%%
import datetime

print("My name is Md. Readul Islam")

today = datetime.date.today()
print(f"Today's date is {today}")

#%%
from utils import add, subtract

print("Add:", add(5, 10))
print("Subtract:", subtract(10, 5))