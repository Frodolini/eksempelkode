from yr.libyr import Yr

#min_dict = {1:{10:11,12:13},3:4}
#print(min_dict[1][12])

weather = Yr(location_name='Norge/Hordaland/Stord/Stord')
now = weather.now()

print("Temperaturen er", now["temperature"]["@value"],"grader Celcius på Stord!")