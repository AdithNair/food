burger = ImageTk.PhotoImage(Image.open ("burger1.png"))
burger_image=Label(root)
burger_image["image"]=burger
burger_image.place(relx=0.7, rely=0.5,anchor=CENTER)
label_heading=Label(root,text="Rdonalds", font=("times",40,"bold"),fg="Orange")
label_heading.place(relx=0.12, rely=0.1,anchor=CENTER)
label_select_dish=Label(root,text="Select Dish",font=("times",15))
label_select_dish.place(relx=0.06, rely=0.2,anchor=CENTER)
dish=["burger", "iced_americano"]
dish_dropdown = ttk.Combobox(root ,state = "readonly",values = dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)
label_select_addons=Label(root,text="Select Add-Ons",font=("times",15))
label_select_addons.place(relx=0.08, rely=0.5,anchor=CENTER)
toppings=[]
toppings_dropdown = ttk.Combobox(root ,state = "readonly",values = toppings)
toppings_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)
dish_amount=Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75,anchor=CENTER)

child1_object =child1(dish_dropdown.get())
child1_object.get_menu()

child2_object =child2(toppings_dropdown.get(),dish_dropdown.get())
child2_object.get_final_amount()

btn_addons = Button(root,text="Check Add-Ons",command=child1_object.get_menu,bg="Blue", fg="white",relief = FLAT)
btn_addons.place(relx=0.06, rely=0.3, anchor=CENTER)

btn_amount = Button(root,text="Amount",command=child2_object.get_final_amount,bg="Blue", fg="white",relief = FLAT)
btn_amount.place(relx=0.04,rely=0.6, anchor=CENTER)
root.mainloop()
