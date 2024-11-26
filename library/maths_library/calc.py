from maths_library import my_maths
page = 1
while True:
	while page == 1:
		choice = -1
		print("Page",page,"============")
		print("Choose an equation:")
		print("0. Exit")
		print("1: Square area")
		print("2: Rectangle area")
		print("3: Triangle area")
		print("4: Circle area")
		print("5. Cuboid area")
		print("6. Cuboid surface area")
		print("7. Next")
		print("==================")
		choice = input("> ")
		
		if choice == "0": # Exit
			print("Exiting...")
			quit()
			
		elif choice == "1": # Square Area
			length = input("Enter square length\n> ")
			print("Area:",(my_maths.area_square(length)))
			accept = input("Press any key to continue\n> ")

		elif choice == "2": # Rectangle Area
			width_height = input("Enter rectangle width and height (X Y)\n> ").split(" ")
			print("Area:",(my_maths.area_rectangle(width_height[0], width_height[1])))
			accept = input("Press any key to continue\n> ")

		elif choice == "3": # Triangle Area
			width_height = input("Enter triangle width and height (X Y)\n> ").split(" ")
			print("Area:",(my_maths.area_triangle(width_height[0], width_height[1])))
			accept = input("Press any key to continue\n> ")

		elif choice == "4": # Circle Area
			radius = input("Enter circle radius\n> ")
			print("Area:",(my_maths.area_circle(radius)))
			accept = input("Press any key to continue\n> ")

		elif choice == "5": # Cube Area
			xyz = input("Enter cube x, y and z (X Y Z)\n> ").split()
			print("Area:",(my_maths.area_cuboid(xyz[0], xyz[1], xyz[2])))
			accept = input("Press any key to continue\n> ")
		
		elif choice == "6": # Cube surface area
			xyz = input("Enter cube x, y and z (X Y Z)\n> ").split()
			print("Surface area:",(my_maths.surface_area_cuboid(xyz[0], xyz[1], xyz[2])))
			accept = input("Press any key to continue\n> ")
		
		elif choice == "7": # Page 1-2
			page = 2
		else:
			print("Invalid input, please try again")
	
	while page == 2:
		print("Page",page,"============")
		print("Choose an equation:")
		print("8. Previous")
		print("9: Sphere volume")
		print("10: Null")
		print("11: Null")
		print("12: Null")
		print("13. Null")
		print("14. Null")
		print("15. Next")
		print("==================")
		choice = input("> ")

		if choice == "8": # Page 2-1
			page = 1
		
		elif choice == "9": # Sphere Volume
			radius = input("Enter sphere radius\n> ")
			print("Volume:",(my_maths.sphere_volume(radius)))
			accept = input("Press any key to continue\n> ")