import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("C:\\Users\\DELL\\Downloads\\customer_purchase_behaviour_dataset.xlsx")

# data cleaning:-
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.info())
print(df.describe())
print(df["City"].unique())

# Functionalities:-
print("\n== Customer with Highest Product Purchases ==\n")
max_quantity=df["Quantity"].max()
top_customers_qnt=df[max_quantity == df["Quantity"]]
print(top_customers_qnt[["CustomerID","Quantity"]])

print("\n== Customer with Lowest Product Purchases == \n")
min_quantity=df["Quantity"].min()
lowest_customers_qnt=df[min_quantity == df["Quantity"]]
print(lowest_customers_qnt[["CustomerID","Quantity"]])

df["revenue"]=df["Price"]*df["Quantity"]
print("\n== Highest Spending Customer ==\n")
a = df["revenue"].idxmax()
top_spend_cust = df.loc[a, ["CustomerID","revenue","Product"]]
print(top_spend_cust)

print("\n== Lowest Spending Customer ==\n")
b = df["revenue"].idxmin()
low_spend_cust = df.loc[b, ["CustomerID","revenue","Product"]]
print(low_spend_cust)

print("\n== Customers with Average Spending Range ==\n")
c = df["revenue"].mean()
avg_spend_cust = df[(c-10000 < df["revenue"]) & (df["revenue"]< c+10000)]
print(avg_spend_cust[["CustomerID","revenue","Product"]])

print("\n== Payment Method Analysis ==\n")
d=df.groupby("PaymentMethod")["OrderID"].count()
print(d)

Top_payment_mtd=d.idxmax()
least_payment_mtd=d.idxmin()
print(f"\nMost Used Payment Method is: {Top_payment_mtd}")
print(f"least Used Payment Method is: {least_payment_mtd}\n")

print("\n==  Category Purchase Trends ==\n")
cate_revenue=df.groupby("Category")["revenue"].sum()
print(cate_revenue)
print(f"\nHighest revenue Category is:{cate_revenue.idxmax()}")
print(f"Lowest revenue Category is:{cate_revenue.idxmin()}")

print("\n=== Gender Purchase Analysis ===\n")
gen_revenue=df.groupby("Gender")["revenue"].sum()
print(gen_revenue)
print(f"\nHigest Revenue Produce Gender is:{gen_revenue.idxmax()}")
print(f"Lowest Revenue Produced Gender is:{gen_revenue.idxmin()}\n")

gen_qnt=df.groupby("Gender")["Quantity"].sum()
print(gen_qnt)
print(f"\nHighest Product Buy by:{gen_qnt.idxmax()}")
print(f"Lowest Product Buy by:{gen_qnt.idxmin()}\n")

print("\n== Gender Category Preference ==\n")
gen_cate=df.groupby(["Gender","Category"])["Quantity"].sum()
print(gen_cate)
print(f"\nMost Preferred Category: {gen_cate.idxmax()}")
print(f"Least Preferred Category: {gen_cate.idxmin()}\n")

print("\n== Age Group Analysis ==\n")
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[18,25,35,45],
    labels=["Young","Adult","Mature"]
)
age_cate=df.groupby(["AgeGroup","Category"],observed=False)["Quantity"].sum() ##  observed=False ye future warning ko durr krne ke liye lgaya hai
print(age_cate)
print(f"\nMost Purchased Category:{age_cate.idxmax()}")
print(f"\nLeast Purchased Category:{age_cate.idxmin()}")

print("\n== City-wise Customer Behaviour ==\n")
city_revenue=df.groupby("City")["revenue"].sum()
print(city_revenue)
print(f"Top city by revenue is:{city_revenue.idxmax()}")
print(f"Lowest city by revenue is:{city_revenue.idxmin()}")

print("\n== Product Performance Analysis ==\n")
product_quantity = df.groupby("Product")["Quantity"].sum()
print("Product Sales (Quantity):")
print(product_quantity)
print(f"\nTop Selling Product: {product_quantity.idxmax()}")
print(f"Lowest Selling Product: {product_quantity.idxmin()}")

product_revenue = df.groupby("Product")["revenue"].sum()
print("\nProduct Revenue:")
print(product_revenue)
print(f"\nHighest Revenue Product: {product_revenue.idxmax()}")
print(f"Lowest Revenue Product: {product_revenue.idxmin()}")

# Dashboard:-

print("\n====== DASHBOARD ======\n")

total_customers = df["CustomerID"].nunique()
total_orders = df["OrderID"].nunique()
total_revenue = df["revenue"].sum()
total_products = df["Quantity"].sum()

print(f"Total Customers: {total_customers}")
print(f"Total Orders: {total_orders}")
print(f"Total Revenue: {total_revenue}")
print(f"Total Products Sold: {total_products}\n")

print(f"Highest Spending Customer: {top_spend_cust['CustomerID']}")
print(f"Highest Purchasing Customer: \n{top_customers_qnt[['CustomerID','Quantity']]}\n")

print(f"Most Used Payment Method: {Top_payment_mtd}")
print(f"Top Revenue Category: {cate_revenue.idxmax()}")
print(f"Top Revenue City: {city_revenue.idxmax()}\n")

print(f"Top Selling Product: {product_quantity.idxmax()}")
print(f"Highest Revenue Product: {product_revenue.idxmax()}\n")

print(f"Highest Revenue Producing Gender: {gen_revenue.idxmax()}")
print(f"Most Purchased Age Group Category: {age_cate.idxmax()}")

# Visualization:-

plt.pie(d.values,labels=d.index,autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.show()

plt.bar(cate_revenue.index, cate_revenue.values,  color=["red","blue","green","orange","purple"])
plt.title("Category Revenue")
plt.xticks(rotation=45)
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()


plt.bar(city_revenue.index, city_revenue.values,color=["cyan","yellow","pink","lime","magenta"])
plt.title("City-wise Revenue")
plt.xticks(rotation=45)
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()


product_revenuee = product_revenue.sort_values( ascending=False).head(5)
plt.barh(product_revenuee.index, product_revenuee.values, color=["gold","silver","coral","skyblue","violet"])
plt.title("Top 5 Revenue Products")
plt.xlabel("Revenue")
plt.ylabel("Products")
plt.show()

plt.barh( [str(i) for i in gen_cate.index],gen_cate.values,color=["red","blue","green","orange","purple","cyan","pink","gold","lime","magenta"])
plt.title("Gender Purchase Analysis")
plt.xlabel("Products Purchased")
plt.ylabel("Gender - Category")
plt.tight_layout() # labels properly dikhte hain, title cut nahi hota, graph clean lagta hai
plt.show()

plt.barh([str(i) for i in age_cate.index],age_cate.values,color=["red","blue","green","orange","purple","cyan","pink","gold","lime","magenta"])
plt.title("Age Group Analysis")
plt.xlabel("Products Purchased")
plt.ylabel("Age Group - Category")
plt.tight_layout()
plt.show()

product_quantityy = product_quantity.sort_values( ascending=False).head(5)
plt.barh(product_quantityy.index, product_quantityy.values, color=["gold","silver","coral","skyblue","violet"])
plt.title("Top 5 Products (Quantity)")
plt.xlabel("Quantity")
plt.ylabel("Products")
plt.show()





