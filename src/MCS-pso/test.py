if __name__ == '__main__':
    particles = [
        [10.0, 49.0, 92.0, 26.0, 44.0, 100.0, 22.0, 2.0, 77.0, 62.0, 46.0, 35.0, 0.0, 32.0, 6.0, 5.0, 67.0, 57.0, 44.0,
         0.0, 68.0, 89.0, 23.0, 35.0, 3.0, 0.0, 33.0, 6.0, 29.0, 11.0, 12.0, 3.0, 3.0, 54.0, 13.0, 3.0, 30.0, 3.0, 8.0,
         2.0, 9.0, 1.0, 2.0, 1.0, 6.0, 8.0, 5.0, 13.0, 5.0, 7.0, 2.0, 9.0, 6.0, 3.0, 10.0, 0.0, 9.0, 4.0, 24.0, 16.0,
         13.0, 9.0, 8.0, 9.0, 3.0, 5.0, 0.0, 24.0, 28.0, 17.0, 31.0],
        [82.0, 78.0, 65.0, 88.0, 56.0, 67.0, 71.0, 51.0, 66.0, 67.0, 17.0, 64.0, 27.0, 91.0, 6.0, 52.0, 71.0, 36.0,
         55.0, 0.0, 26.0, 69.0, 83.0, 97.0, 37.0, 0.0, 7.0, 2.0, 3.0, 11.0, 32.0, 1.0, 7.0, 38.0, 5.0, 31.0, 26.0, 3.0,
         2.0, 12.0, 5.0, 9.0, 1.0, 6.0, 1.0, 11.0, 4.0, 16.0, 13.0, 4.0, 2.0, 4.0, 2.0, 4.0, 1.0, 0.0, 11.0, 3.0, 40.0,
         2.0, 6.0, 2.0, 2.0, 7.0, 6.0, 21.0, 0.0, 24.0, 5.0, 60.0, 11.0],
        [79.0, 42.0, 60.0, 19.0, 24.0, 90.0, 27.0, 87.0, 87.0, 64.0, 81.0, 80.0, 73.0, 32.0, 61.0, 29.0, 17.0, 50.0,
         56.0, 0.0, 76.0, 36.0, 82.0, 96.0, 4.0, 0.0, 3.0, 10.0, 4.0, 46.0, 19.0, 3.0, 11.0, 38.0, 2.0, 30.0, 30.0, 7.0,
         3.0, 8.0, 1.0, 1.0, 13.0, 13.0, 9.0, 3.0, 7.0, 6.0, 1.0, 2.0, 3.0, 3.0, 11.0, 6.0, 3.0, 0.0, 10.0, 12.0, 9.0,
         5.0, 3.0, 1.0, 7.0, 6.0, 28.0, 19.0, 0.0, 3.0, 22.0, 44.0, 31.0],
        [66.0, 92.0, 57.0, 38.0, 31.0, 79.0, 67.0, 62.0, 93.0, 51.0, 55.0, 38.0, 1.0, 99.0, 75.0, 30.0, 14.0, 31.0,
         85.0, 0.0, 59.0, 22.0, 28.0, 64.0, 5.0, 0.0, 14.0, 1.0, 4.0, 26.0, 5.0, 19.0, 26.0, 28.0, 38.0, 29.0, 5.0, 5.0,
         1.0, 1.0, 3.0, 11.0, 19.0, 10.0, 6.0, 2.0, 1.0, 2.0, 5.0, 1.0, 5.0, 4.0, 13.0, 4.0, 7.0, 0.0, 21.0, 11.0, 4.0,
         10.0, 6.0, 7.0, 4.0, 25.0, 2.0, 10.0, 0.0, 57.0, 11.0, 13.0, 19.0],
        [25.0, 2.0, 75.0, 100.0, 79.0, 57.0, 99.0, 67.0, 24.0, 15.0, 26.0, 56.0, 43.0, 93.0, 92.0, 82.0, 72.0, 0.0,
         32.0, 0.0, 95.0, 72.0, 66.0, 21.0, 28.0, 0.0, 16.0, 6.0, 12.0, 13.0, 5.0, 19.0, 1.0, 40.0, 29.0, 4.0, 27.0,
         3.0, 27.0, 4.0, 2.0, 9.0, 5.0, 23.0, 1.0, 3.0, 2.0, 3.0, 1.0, 3.0, 1.0, 3.0, 1.0, 4.0, 5.0, 0.0, 9.0, 3.0,
         35.0, 6.0, 9.0, 4.0, 2.0, 18.0, 3.0, 11.0, 0.0, 8.0, 34.0, 36.0, 22.0],
        [0.0, 76.0, 19.0, 81.0, 14.0, 15.0, 83.0, 51.0, 72.0, 56.0, 24.0, 36.0, 67.0, 92.0, 67.0, 34.0, 32.0, 22.0,
         29.0, 0.0, 75.0, 96.0, 41.0, 23.0, 7.0, 0.0, 13.0, 6.0, 14.0, 1.0, 20.0, 7.0, 32.0, 10.0, 15.0, 16.0, 59.0,
         1.0, 1.0, 5.0, 4.0, 5.0, 15.0, 1.0, 1.0, 5.0, 1.0, 3.0, 8.0, 25.0, 1.0, 6.0, 3.0, 3.0, 12.0, 0.0, 6.0, 7.0,
         17.0, 4.0, 8.0, 7.0, 12.0, 21.0, 5.0, 13.0, 0.0, 29.0, 18.0, 33.0, 20.0],
        [96.0, 4.0, 84.0, 100.0, 86.0, 7.0, 2.0, 26.0, 24.0, 20.0, 8.0, 100.0, 88.0, 59.0, 86.0, 56.0, 63.0, 71.0, 54.0,
         0.0, 49.0, 61.0, 40.0, 93.0, 17.0, 0.0, 2.0, 9.0, 7.0, 18.0, 5.0, 38.0, 4.0, 12.0, 12.0, 66.0, 10.0, 2.0, 9.0,
         8.0, 4.0, 12.0, 4.0, 8.0, 5.0, 3.0, 21.0, 3.0, 1.0, 5.0, 4.0, 1.0, 2.0, 1.0, 7.0, 0.0, 14.0, 2.0, 1.0, 10.0,
         10.0, 21.0, 9.0, 5.0, 4.0, 24.0, 0.0, 3.0, 25.0, 47.0, 25.0],
        [40.0, 38.0, 50.0, 88.0, 93.0, 5.0, 31.0, 90.0, 55.0, 74.0, 55.0, 1.0, 2.0, 80.0, 19.0, 77.0, 33.0, 50.0, 58.0,
         0.0, 29.0, 46.0, 81.0, 8.0, 2.0, 0.0, 16.0, 11.0, 6.0, 33.0, 17.0, 13.0, 2.0, 44.0, 38.0, 5.0, 13.0, 3.0, 2.0,
         4.0, 5.0, 8.0, 12.0, 1.0, 4.0, 14.0, 3.0, 1.0, 15.0, 3.0, 1.0, 12.0, 9.0, 2.0, 1.0, 0.0, 4.0, 2.0, 32.0, 5.0,
         2.0, 15.0, 2.0, 13.0, 21.0, 4.0, 0.0, 6.0, 30.0, 62.0, 2.0],
        [6.0, 29.0, 96.0, 76.0, 31.0, 95.0, 76.0, 74.0, 23.0, 68.0, 66.0, 17.0, 57.0, 27.0, 0.0, 66.0, 45.0, 50.0, 98.0,
         0.0, 56.0, 39.0, 53.0, 72.0, 12.0, 0.0, 6.0, 4.0, 8.0, 39.0, 4.0, 2.0, 25.0, 1.0, 33.0, 15.0, 51.0, 1.0, 7.0,
         6.0, 12.0, 1.0, 2.0, 4.0, 6.0, 14.0, 4.0, 2.0, 3.0, 5.0, 11.0, 2.0, 2.0, 10.0, 8.0, 0.0, 16.0, 8.0, 9.0, 10.0,
         20.0, 15.0, 1.0, 14.0, 4.0, 3.0, 0.0, 51.0, 9.0, 3.0, 37.0],
        [51.0, 47.0, 89.0, 79.0, 7.0, 11.0, 39.0, 67.0, 19.0, 71.0, 51.0, 14.0, 49.0, 54.0, 64.0, 92.0, 30.0, 32.0,
         42.0, 0.0, 22.0, 0.0, 54.0, 40.0, 5.0, 0.0, 10.0, 13.0, 13.0, 7.0, 8.0, 36.0, 8.0, 11.0, 11.0, 1.0, 77.0, 4.0,
         2.0, 1.0, 4.0, 9.0, 12.0, 4.0, 3.0, 8.0, 1.0, 8.0, 1.0, 15.0, 4.0, 2.0, 10.0, 10.0, 2.0, 0.0, 20.0, 5.0, 1.0,
         5.0, 10.0, 9.0, 6.0, 14.0, 7.0, 23.0, 0.0, 4.0, 5.0, 2.0, 89.0]]
    velocities = [
        [74, 74, -41, 77, 32, 36, 38, 50, -100, 0, 13, 51, 18, 21, 53, 33, -40, -1, 43, 0, -89, -3, 80, 34, 43, 0, -33,
         24, 40, 6, 85, 96, 88, -32, 53, 91, 58, 82, 90, 57, 55, 26, 16, 86, 21, -11, 11, 40, 43, 31, 72, 51, 58, 74,
         60, 0, 75, 30, 0, 57, 64, 38, 47, 37, 29, 85, 0, 38, -18, 84, 1],
        [-52, -151, 0, -35, -88, 55, -62, -40, 69, 7, 92, -51, -37, -52, 19, -40, 76, 44, -25, 0, 58, 74, -110, -206,
         -17, 0, 84, 47, 86, 70, -16, 14, 63, 29, 20, -23, -34, 47, 68, 54, -2, 38, 47, 75, 4, 36, 55, 7, 47, 83, 73,
         44, 61, 60, 28, 0, 34, 28, -35, 79, 92, 10, 93, 33, 88, 81, 0, 56, 47, -73, 42],
        [56, 53, 41, 22, 67, 31, 14, -103, 34, -67, -112, -110, -18, 2, 9, 29, 70, 10, 55, 0, -81, 80, -45, -50, 79, 0,
         106, 58, 27, -93, 14, 0, -9, -18, 16, -38, 73, 23, 25, 28, 12, 6, 57, 24, -2, 3, 49, 25, 57, 64, 49, 1, 74, 55,
         13, 0, 80, -1, -12, 33, 33, 98, 80, 1, 44, -9, 0, 43, 0, -109, 96],
        [-35, -110, 62, -12, 19, 41, -7, -19, 13, -41, -36, 13, 23, -75, -182, 5, 69, 90, -137, 0, -5, 146, 44, -52, 3,
         0, 9, 92, 104, 61, 22, 13, 12, 16, -1, 24, 81, 61, 84, 71, 9, 71, 15, 50, 34, 41, 5, 79, 65, 92, 17, 40, 75,
         38, -3, 0, 24, -13, 37, 39, 14, 98, 16, -13, 55, 20, 0, -58, 51, 72, -3],
        [-49, 122, 91, -203, 62, 12, -29, 8, 120, 88, 12, -7, -128, -65, -272, 18, -48, 88, -23, 0, -64, 4, -50, 70,
         -30, 0, 43, 6, 62, 68, 24, 55, 3, 51, 0, 59, -24, 43, -26, 53, 12, 13, 55, 55, 42, 41, 57, 44, 64, 83, 5, 31,
         14, 66, 53, 0, -3, 5, -56, 15, 53, 70, 46, 42, 71, -23, 0, 104, 15, 4, 55],
        [47, -3, 164, -35, 42, 29, -83, -25, 0, -23, 39, -15, -57, -102, -8, -38, 44, 80, 47, 0, -129, 33, -47, -24, 55,
         0, 25, 67, 104, 71, 21, 1, 8, 79, 73, 14, -70, 53, 65, 44, 42, 91, 20, 74, 31, 81, 46, 36, 8, 49, 11, 97, 84,
         93, 63, 0, -2, 24, -11, 116, 25, 88, -6, 34, 19, 19, 0, -29, 77, -3, 91],
        [-180, 28, 18, -60, -176, 59, 110, -10, 93, 85, 35, -180, -214, -4, -221, -82, 71, 59, 23, 0, -56, 77, 19, -18,
         18, 0, 85, 19, 84, -20, 89, -42, 57, 141, 22, -19, 101, 16, 9, -3, 65, 14, 78, 72, 79, 77, 24, 31, 24, 19, 88,
         94, 34, 13, 69, 0, 62, 7, 103, 68, 22, 13, 24, 33, 3, -26, 0, 47, 95, -84, 16],
        [-49, 13, 43, -26, -188, 10, -46, -150, -26, 10, 16, 62, 28, -152, -30, 47, 78, 13, -46, 0, 22, 47, -155, 26,
         67, 0, 72, 57, 101, -73, 12, 13, 62, 19, -18, 63, 10, 63, 80, 72, 33, 75, 21, 13, 41, -22, 6, 85, 43, 78, 51,
         43, 66, 48, 32, 0, 92, 44, 10, 87, 29, 8, 69, 4, -61, 35, 0, 48, -17, -77, 30],
        [78, 43, -96, -109, 71, -70, -13, -104, 65, 0, -40, 20, -158, 55, 35, -122, 4, 57, -77, 0, -14, 83, 11, 13, 54,
         0, 56, 4, 99, -23, 51, 53, 78, 131, -25, 53, -37, 18, 22, 27, 42, 1, 89, 89, 23, 15, 91, 48, 47, 66, -21, 90,
         48, 79, 11, 0, 24, 59, 73, 66, 29, 38, 32, 69, 94, 52, 0, -45, 29, 56, 53],
        [-130, -13, -114, -121, 74, 65, 26, -145, 99, 30, 65, 55, -61, -32, -194, -128, 95, -5, 53, 0, 48, 200, -71,
         -26, 28, 0, 83, -4, 60, 85, 7, 35, 52, 94, 3, 38, -65, 89, 82, 29, 10, 28, 56, 73, 0, 21, 71, 92, 9, -14, 11,
         63, 0, 10, 58, 0, 77, 60, 8, 47, -1, 8, 65, 41, 84, 70, 0, 34, 82, 102, -176]]

    particle_after = [
        [84.0, 100, 51.0, 100, 76.0, 100, 60.0, 52.0, 0, 62.0, 59.0, 86.0, 18.0, 53.0, 59.0, 38.0, 27.0, 56.0, 87.0,
         0.0, 0, 86.0, 100, 69.0, 46.0, 0.0, 0.0, 30.0, 69.0, 17.0, 97.0, 99.0, 91.0, 22.0, 66.0, 94.0, 88.0, 85.0,
         98.0, 59.0, 64.0, 27.0, 18.0, 87.0, 27.0, 0, 16.0, 53.0, 48.0, 38.0, 74.0, 60.0, 64.0, 77.0, 70.0, 0.0, 84.0,
         34.0, 24.0, 73.0, 77.0, 47.0, 55.0, 46.0, 32.0, 90.0, 0.0, 62.0, 10.0, 100, 32.0]
        ,
        [30.0, 0, 65.0, 53.0, 0, 100, 9.0, 11.0, 100, 74.0, 100, 13.0, 0, 39.0, 25.0, 12.0, 100, 80.0, 30.0, 0.0, 84.0,
         100, 0, 0, 20.0, 0.0, 91.0, 49.0, 89.0, 81.0, 16.0, 15.0, 70.0, 67.0, 25.0, 8.0, 0, 50.0, 70.0, 66.0, 3.0,
         47.0, 48.0, 81.0, 5.0, 47.0, 59.0, 23.0, 60.0, 87.0, 75.0, 48.0, 63.0, 64.0, 29.0, 0.0, 45.0, 31.0, 5.0, 81.0,
         98.0, 12.0, 95.0, 40.0, 94.0, 100, 0.0, 80.0, 52.0, 0, 53.0]
        , [100, 95.0, 100, 41.0, 91.0, 100, 41.0, 0, 100, 0, 0, 0, 55.0, 34.0, 70.0, 58.0, 87.0, 60.0, 100, 0.0, 0, 100,
           37.0, 46.0, 83.0, 0.0, 100, 68.0, 31.0, 0, 33.0, 3.0, 2.0, 20.0, 18.0, 0, 100, 30.0, 28.0, 36.0, 13.0, 7.0,
           70.0, 37.0, 7.0, 6.0, 56.0, 31.0, 58.0, 66.0, 52.0, 4.0, 85.0, 61.0, 16.0, 0.0, 90.0, 11.0, 0, 38.0, 36.0,
           99.0, 87.0, 7.0, 72.0, 10.0, 0.0, 46.0, 22.0, 0, 100]
        ,
        [31.0, 0, 100, 26.0, 50.0, 100, 60.0, 43.0, 100, 10.0, 19.0, 51.0, 24.0, 24.0, 0, 35.0, 83.0, 100, 0, 0.0, 54.0,
         100, 72.0, 12.0, 8.0, 0.0, 23.0, 93.0, 100, 87.0, 27.0, 32.0, 38.0, 44.0, 37.0, 53.0, 86.0, 66.0, 85.0, 72.0,
         12.0, 82.0, 34.0, 60.0, 40.0, 43.0, 6.0, 81.0, 70.0, 93.0, 22.0, 44.0, 88.0, 42.0, 4.0, 0.0, 45.0, 0, 41.0,
         49.0, 20.0, 100, 20.0, 12.0, 57.0, 30.0, 0.0, 0, 62.0, 85.0, 16.0]
        , [0, 100, 100, 0, 100, 69.0, 70.0, 75.0, 100, 100, 38.0, 49.0, 0, 28.0, 0, 100.0, 24.0, 88.0, 9.0, 0.0, 31.0,
           76.0, 16.0, 91.0, 0, 0.0, 59.0, 12.0, 74.0, 81.0, 29.0, 74.0, 4.0, 91.0, 29.0, 63.0, 3.0, 46.0, 1.0, 57.0,
           14.0, 22.0, 60.0, 78.0, 43.0, 44.0, 59.0, 47.0, 65.0, 86.0, 6.0, 34.0, 15.0, 70.0, 58.0, 0.0, 6.0, 8.0, 0,
           21.0, 62.0, 74.0, 48.0, 60.0, 74.0, 0, 0.0, 100, 49.0, 40.0, 77.0]
        , [47.0, 73.0, 100, 46.0, 56.0, 44.0, 0.0, 26.0, 72.0, 33.0, 63.0, 21.0, 10.0, 0, 59.0, 0, 76.0, 100, 76.0, 0.0,
           0, 100, 0, 0, 62.0, 0.0, 38.0, 73.0, 100, 72.0, 41.0, 8.0, 40.0, 89.0, 88.0, 30.0, 0, 54.0, 66.0, 49.0, 46.0,
           96.0, 35.0, 75.0, 32.0, 86.0, 47.0, 39.0, 16.0, 74.0, 12.0, 100, 87.0, 96.0, 75.0, 0.0, 4.0, 31.0, 6.0, 100,
           33.0, 95.0, 6.0, 55.0, 24.0, 32.0, 0.0, 0.0, 95.0, 30.0, 100]
        , [0, 32.0, 100, 40.0, 0, 66.0, 100, 16.0, 100, 100, 43.0, 0, 0, 55.0, 0, 0, 100, 100, 77.0, 0.0, 0, 100, 59.0,
           75.0, 35.0, 0.0, 87.0, 28.0, 91.0, 0, 94.0, 0, 61.0, 100, 34.0, 47.0, 100, 18.0, 18.0, 5.0, 69.0, 26.0, 82.0,
           80.0, 84.0, 80.0, 45.0, 34.0, 25.0, 24.0, 92.0, 95.0, 36.0, 14.0, 76.0, 0.0, 76.0, 9.0, 100, 78.0, 32.0,
           34.0, 33.0, 38.0, 7.0, 0, 0.0, 50.0, 100, 0, 41.0]
        ,
        [0, 51.0, 93.0, 62.0, 0, 15.0, 0, 0, 29.0, 84.0, 71.0, 63.0, 30.0, 0, 0, 100, 100, 63.0, 12.0, 0.0, 51.0, 93.0,
         0, 34.0, 69.0, 0.0, 88.0, 68.0, 100, 0, 29.0, 26.0, 64.0, 63.0, 20.0, 68.0, 23.0, 66.0, 82.0, 76.0, 38.0, 83.0,
         33.0, 14.0, 45.0, 0, 9.0, 86.0, 58.0, 81.0, 52.0, 55.0, 75.0, 50.0, 33.0, 0.0, 96.0, 46.0, 42.0, 92.0, 31.0,
         23.0, 71.0, 17.0, 0, 39.0, 0.0, 54.0, 13.0, 0, 32.0]
        , [84.0, 72.0, 0.0, 0, 100, 25.0, 63.0, 0, 88.0, 68.0, 26.0, 37.0, 0, 82.0, 35.0, 0, 49.0, 100, 21.0, 0.0, 42.0,
           100, 64.0, 85.0, 66.0, 0.0, 62.0, 8.0, 100, 16.0, 55.0, 55.0, 100, 100, 8.0, 68.0, 14.0, 19.0, 29.0, 33.0,
           54.0, 2.0, 91.0, 93.0, 29.0, 29.0, 95.0, 50.0, 50.0, 71.0, 0, 92.0, 50.0, 89.0, 19.0, 0.0, 40.0, 67.0, 82.0,
           76.0, 49.0, 53.0, 33.0, 83.0, 98.0, 55.0, 0.0, 6.0, 38.0, 59.0, 90.0]
        , [0, 34.0, 0, 0, 81.0, 76.0, 65.0, 0, 100, 100, 100, 69.0, 0, 22.0, 0, 0, 100, 27.0, 95.0, 0.0, 70.0, 100, 0,
           14.0, 33.0, 0.0, 93.0, 9.0, 73.0, 92.0, 15.0, 71.0, 60.0, 100, 14.0, 39.0, 12.0, 93.0, 84.0, 30.0, 14.0,
           37.0, 68.0, 77.0, 3.0, 29.0, 72.0, 100.0, 10.0, 1.0, 15.0, 65.0, 10.0, 20.0, 60.0, 0.0, 97.0, 65.0, 9.0,
           52.0, 9.0, 17.0, 71.0, 55.0, 91.0, 93.0, 0.0, 38.0, 87.0, 100, 0]]

    for _ in range(10):
        for __ in range(len(particles[_])):
            particles[_][__] += velocities[_][__]

    for _ in range(10):
        for __ in range(len(particles[_])):
            if particles[_][__] > 100:
                particles[_][__] = 100
            if particles[_][__] < 0:
                particles[_][__] = 0

    for _ in range(10):
        print(_)
        for __ in range(0, 24):
            assert particles[_][__] == particle_after[_][__], str(particles[_][__]) + '<==>' + str(particle_after[_][__])

        sum_val = sum(particles[_][24:33])
        for __ in range(24, 33):
            if particles[_][__] != particle_after[_][__]:
                print(str(_) + '-' + str(__) + ':' + str(particles[_][__]) + '<==>' + str(particle_after[_][__]))

        sum_val = sum(particles[_][33:37])
        for __ in range(33, 37):
            if particles[_][__] != particle_after[_][__]:
                print(str(_) + '-' + str(__) + ':' + str(particles[_][__]) + '<==>' + str(particle_after[_][__]))

        sum_val = sum(particles[_][37:55])
        for __ in range(37, 55):
            if particles[_][__] != particle_after[_][__]:
                print(str(_) + '-' + str(__) + ':' + str(particles[_][__]) + '<==>' + str(particle_after[_][__]))

        sum_val = sum(particles[_][55:67])
        for __ in range(55, 67):
            if particles[_][__] != particle_after[_][__]:
                print(str(_) + '-' + str(__) + ':' + str(particles[_][__]) + '<==>' + str(particle_after[_][__]))

        sum_val = sum(particles[_][67:71])
        for __ in range(67, 71):
            if particles[_][__] != particle_after[_][__]:
                print(str(_) + '-' + str(__) + ':' + str(particles[_][__]) + '<==>' + str(particle_after[_][__]))