import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tarfile
import pandas as pd
from dateutil import parser

pd.plotting.register_matplotlib_converters()


def parse_date(df):
    def valid_datetime(date):
        try:
            return parser.parse(date)
        except ValueError:
            print("Invalid date:", date)
            return None

    df['Timestamp'] = df['Timestamp'].apply(valid_datetime)
    return df


def clean_timestamp(df):
    df = df[df["Timestamp"] != None]
    return df


def tableauDeBord():

    # data retrieve
    mytargz = tarfile.open('clean.tar.gz', "r:gz")
    csv_path = 'clean/01. Duc/2014-11-14 09:40:00.csv.gz'
    df = pd.read_csv(mytargz.extractfile(csv_path), header=0, sep=";", compression='gzip')


    # data resampling
    df = parse_date(df)
    df = clean_timestamp(df)
    df = df.set_index('Timestamp').resample('H', label='right', closed='right').last().dropna()

    days = mdates.DayLocator()
    hours = mdates.HourLocator()

    fig, ax = plt.subplots(2,3)

    # plot of the slots and bikes
    slotplot = ax[0, 0]
    barWidth = 0.06
    slots = slotplot.bar(df.index, df['Slots'], barWidth)
    bikes = slotplot.bar(df.index, df['Bikes'], barWidth)

    slotplot.set_ylabel("Nombre de slots")
    slotplot.set_xlabel("Temps en heures")
    slotplot.legend((slots, bikes), ('Total slots', 'Total velos'))
    slotplot.title.set_text("Occupation des slots en fonction du temps")

    slotplot.xaxis.set_major_locator(days)
    slotplot.xaxis.set_minor_locator(hours)


    # humidity plot
    humidityplot = ax[0, 1]
    humidityplot.plot(df.index, df['Humidity'])

    humidityplot.grid(True)
    humidityplot.set_xlabel("Temps en heures")
    humidityplot.set_ylabel("Pourcentage d'humidité")
    humidityplot.title.set_text("Humidité en fonction du temps")
    humidityplot.xaxis.set_major_locator(days)
    humidityplot.xaxis.set_minor_locator(hours)

    # pressure plot
    pressureplot = ax[0, 2]
    pressureplot.plot(df.index, df['Pressure'], linewidth=0, marker='.', markersize=5)
    # pressureplot.scatter(df.index, df['Pressure'])

    pressureplot.grid(True)
    pressureplot.set_xlabel("Temps en heures")
    pressureplot.set_ylabel("Pression en hPa")
    pressureplot.title.set_text("Pression en fonction du temps")
    pressureplot.xaxis.set_major_locator(days)
    pressureplot.xaxis.set_minor_locator(hours)

    # windeg plot
    windegplot = ax[1, 0]
    windegplot.plot(df.index, df['WindDeg'])
    # windegplot.plot(df.index, df['WindDeg'], linewidth=0, marker='.', markersize=5)

    windegplot.grid(True)
    windegplot.set_xlabel("Temps en heures")
    windegplot.title.set_text("Windeg en fonction du temps")
    windegplot.xaxis.set_major_locator(days)
    windegplot.xaxis.set_minor_locator(hours)

    # windspeed plot
    winspeedplot = ax[1, 1]
    winspeedplot.plot(df.index, df['WindSpeed'])

    winspeedplot.grid(True)
    winspeedplot.set_xlabel("Temps en heures")
    winspeedplot.title.set_text("Windspeed en fonction du temps")
    winspeedplot.xaxis.set_major_locator(days)
    winspeedplot.xaxis.set_minor_locator(hours)

    # temperature plot
    tempplot = ax[1, 2]

    tempplot.plot(df.index, df['TemperatureTemp'])

    tempplot.grid(True)
    tempplot.set_xlabel("Temps en heures")
    tempplot.set_ylabel("Température en °C")
    tempplot.title.set_text("Température en fonction du temps")
    tempplot.xaxis.set_major_locator(days)
    tempplot.xaxis.set_minor_locator(hours)

    fig.autofmt_xdate()
    plt.suptitle("Tableau de bord")
    plt.show()


def tableauDeBordSepare():

    # data retrieve
    mytargz = tarfile.open('clean.tar.gz', "r:gz")
    csv_path = 'clean/01. Duc/2014-11-14 09:40:00.csv.gz'
    df = pd.read_csv(mytargz.extractfile(csv_path), header=0, sep=";", compression='gzip')


    # data resampling
    df = parse_date(df)
    df = clean_timestamp(df)
    df = df.set_index('Timestamp').resample('H', label='right', closed='right').last().dropna()

    days = mdates.DayLocator()
    hours = mdates.HourLocator()

    # plot of the slots and bikes
    barWidth = 0.06
    slots = plt.bar(df.index, df['Slots'], barWidth)
    bikes = plt.bar(df.index, df['Bikes'], barWidth)

    plt.ylabel("Nombre de slots")
    plt.xlabel("Temps en heures")
    plt.legend((slots, bikes), ('Total slots', 'Total velos'))
    plt.title("Occupation des slots en fonction du temps")

    plt.axes().xaxis.set_major_locator(days)
    plt.axes().xaxis.set_minor_locator(hours)

    plt.show()


    # humidity plot
    plt.plot(df.index, df['Humidity'])

    plt.grid(True)
    plt.xlabel("Temps en heures")
    plt.ylabel("Pourcentage d'humidité")
    plt.title("Humidité en fonction du temps")
    plt.axes().xaxis.set_major_locator(days)
    plt.axes().xaxis.set_minor_locator(hours)

    plt.show()

    # pressure plot
    plt.plot(df.index, df['Pressure'], linewidth=0, marker='.', markersize=5)
    # pressureplot.scatter(df.index, df['Pressure'])

    plt.grid(True)
    plt.xlabel("Temps en heures")
    plt.ylabel("Pression en hPa")
    plt.title("Pression en fonction du temps")
    plt.axes().xaxis.set_major_locator(days)
    plt.axes().xaxis.set_minor_locator(hours)

    plt.show()

    # windeg plot
    plt.plot(df.index, df['WindDeg'])
    # plt.plot(df.index, df['WindDeg'], linewidth=0, marker='.', markersize=5)

    plt.grid(True)
    plt.xlabel("Temps en heures")
    plt.title("Windeg en fonction du temps")
    plt.axes().xaxis.set_major_locator(days)
    plt.axes().xaxis.set_minor_locator(hours)

    plt.show()

    # windspeed plot
    plt.plot(df.index, df['WindSpeed'])

    plt.grid(True)
    plt.xlabel("Temps en heures")
    plt.title("Windspeed en fonction du temps")
    plt.axes().xaxis.set_major_locator(days)
    plt.axes().xaxis.set_minor_locator(hours)

    plt.show()

    # temperature plot
    plt.plot(df.index, df['TemperatureTemp'])

    plt.grid(True)
    plt.xlabel("Temps en heures")
    plt.ylabel("Température en °C")
    plt.title("Température en fonction du temps")
    plt.axes().xaxis.set_major_locator(days)
    plt.axes().xaxis.set_minor_locator(hours)
    plt.show()


tableauDeBord()
# tableauDeBordSepare()