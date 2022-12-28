import asyncio
import os
import python_weather


async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL, ) as client:
        # Specify the name of the city we need.
        city_name = str(input('Print tne name city: '))
        weather = await client.get(city_name)
        temperature = (weather.current.temperature - 32) / 1.8
        # We display the name city and the temperature in it.
        print(f'Temperature in {city_name} is now {round(temperature)} degrees.')


if __name__ == '__main__':

    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    asyncio.run(getweather())
input()