import sphereutils

def main():
    volume = 5.0
    radius = sphereutils.calcradius(volume)
    area = sphereutils.calcarea(volume,radius)

    print(f'radius: {radius} area: {area}')
    

if __name__ == "__main__":
    main()
