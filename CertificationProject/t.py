class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
        
    def get_balance(self):
        return self.balance
    
    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False
    
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {other_category.name}'})
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
    
    def __str__(self):
        output = self.name.center(30, '*') + "\n"
        for item in self.ledger:
            amount = item['amount']
            description = item['description']
            output += f"{description[0:23]:<23}{amount:7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    spending_in_each = []
    total_spent = 0

    for category in categories:
        category_total = 0
        for i in category.ledger:
            if i["amount"] < 0:
                category_total += abs(i["amount"])

        spending_in_each.append(category_total)
        total_spent += category_total

    percents = []
    
    for spent in spending_in_each:
        if total_spent > 0:
            percent = (spent / total_spent) * 100
            # Round down to nearest multiple of 10
            percents.append(int(percent / 10) * 10)
        else:
            percents.append(0)

    x_axis = [100,90,80,70,60,50,40,30,20,10,0]

    #Returns the x axis with o's symbolizing the percentages
    chart = "Percentage spent by category"
    for i in x_axis:
        chart += f"\n{str(i).rjust(3)}|"
        for p in percents:
            if p >= i:
                chart += "o"
            else:
                chart += " "
            chart += "  "  # 2 spaces after each bar/space
        chart += " "  # 1 extra space at the end
    
    chart += "\n    " + "-" * (len(categories) * 3 + 1)


    chart += "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        chart += "     "  # 5 spaces for alignment
        
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len -1:
            chart += "\n"
    return chart





food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10, 'gucci')
create_spend_chart([food,clothing])
print(food)