def area_weather_condition():
    print("\n\t\t\tBelow ae regions with their weather conditions. ")
    print("1. Central Region")
    print("2. Rift Valley Region")
    print("3. Western Kenya  Region")
    print("4. Eastern Kenya  Region")
    print("5. Nyanza  Region")
    print("6. Coast  Region")
    print("7. Nairobi Region")
    print("8. Northern Kenya Region")



def main():
    area_weather_condition()
    region = input("Enter your region(1-8): ")
    match region:
        case "1":
            print('''
You have to put on heavy clothes due to the cold conditions in the region.
Put on gumboots when it is rainy/muddy.
            ''')

        case "2":
            print('''
The place is at times cold and sometimes it is hot.
When cold put on heavy clothes and when hot put on light clothes.
                ''')

        case "3":
            print('''
There are mosquitoes. It is therefore advisable to ensure you use the protective nets.
Avoid water stagnant areas as they give sites for mosquito breeding            
            ''')

        case "4":
            print('''
The place is arid as well as semi-arid.
Be careful when nomad as one can be bitten by a snake.
Put on light clothes when it is hot and avoid staying under the direct sun            
            ''')

        case "5":
            print('''
Places like Kisumu are humid due to the presence of the lake. Hence, the area is rainy. 
Wear the appropriate clothes to keep away from the cold.
            ''')

        case "6":
            print('''
The area is famous for its hot but relaxing weather.
Put on sun glasses to avoid direct sun and wear the anti-sunshine lotion to prevent burns by sun.
            ''')

        case "7":
            print('''
There is a lot of rain. Hence dress appropriately.
During the times when the sun is hot, wear as needed to avoid overheating. 
            ''')

        case "8":
            print('''
The area is soo hot. Put on very light clothes.
Ensure you drink water constantly to avoid dehydration.
At night- The weather is cold. Put on heavy clothe sto ensure you are not affected by the night cold.
            ''')

        case _ :
            print("Invalid region. Please try again")








if __name__ == '__main__':
    main()