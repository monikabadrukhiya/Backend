# 1.pattern =====================
# for i in range(1,6):                                      #1
#     for j in range(1,i+1):                                #12
#         print(j,end="")                                   #123
# print()                                                   #1234
                                                            #12345   
# 2.pattern ======================
# for i in range(5,0,-1):                                   #5
#     for j in range(5,i-1,-1):                             #54
#         print(j,end="")                                   #543
#     print()                                               #5432
                                                            #54321
# 3.pattern =======================
# for i in range(6,0,-1):                                   #12345
#     for j in range(1,i):                                  #1234
#         print(j,end="")                                   #123
#     print()                                               #12
                                                            #1
# 4. pattern =====================
# for i in range(1,6):                                      #1
#     for j in range(i,0,-1):                               #21
#         print(j,end="")                                   #321
#     print()                                               #4321
                                                            #54321
# 5.pattern======================
# for i in range(0,6):                                        #54321
#     for j in range(5,i,-1):                                 #5432
#         print(j,end="")                                     #543
#     print()                                                 #54
#                                                             #5
# 6. pattern =====================
# for i in range(5,0,-1):                                      #5
#     for j in range(i,5+1):                                   #45
#         print(j,end="")                                      #345
#     print()                                                  #2345
                                                               #12345
# 7. pattern =====================
# for i in range(0,5+1):                                       #54321
#     for j in range(5-i,0,-1):                                #4321
#         print(j,end="")                                      #321
#     print()                                                  #21
                                                               #1 
# 8.pattern ======================
# for i in range(1,6):                                         #12345
#     for j in range(i,6):                                     #2345
#         print(j,end="")                                      #345
#     print()                                                  #45
                                                               #5 
#  9.pattern ======================
# for i in range(5,0,-1):                                       #5
#     for j in range(i,6):                                      #44
#         print(i,end="")                                       #333
#     print()                                                   #2222
                                                                #11111
# 10 pattern ======================
# for i in range(1,6):                                          #1
#     for j in range(0,i):                                      #22   
#         print(i,end="")                                       #333
#     print()                                                   #4444
                                                                #55555
# 11 .pattern ====================
# for i in range(1,6):                                          #     1
#     for k in range(5,i,-1):                                   #    12
#         print(end=" ")                                        #   123    
#     for j in range(1,i+1):                                    #  1234
#         print(j,end="")                                       # 123345
#     print()

# 12. pattern ====================
# for i  in range(6,0,-1):                                     # 12345
#     for k in range(6,i,-1):                                  #  1234
#         print(end=" ")                                       #   123
#     for j in range(1,i):                                     #    12
#         print(j,end="")                                      #     1
#     print()                                                    

# 13.pattern ======================
# for i in range(1,6):                                        # 12345
#     for k in range(0,i):                                    #  2345
#         print(end=" ")                                      #   345
#     for j in range(i,6):                                    #    45
#         print(j,end="")                                     #     5
#     print()

#  14. pattern =====================
# for i in range(5,0,-1):                                   #    5
#     for k in range(i,1,-1):                               #   45
#         print(end=" ")                                    #  345
#     for j in range(i,6):                                  # 2345
#         print(j,end="")                                   #12345
#     print()

# 15. pattern ======================
# for i in range(1,6):                                      #    1
#     for k in range(5,i,-1):                               #   21
#         print(end=" ")                                    #  321
#     for j in range(i,0,-1):                               # 4321
#         print(j,end="")                                   #54321
#     print()

# 16.pattern =========================
# for i in range(5,0,-1):                                   #54321
#     for k in range(6,i+1,-1):                             # 4321
#         print(end=" ")                                    #  321
#     for j in range(i,0,-1):                               #   21
#         print(j,end="")                                   #    1
#     print()

# 17.pattern =========================
# for i in range(0,6):                                      #54321
#     for k in range(1,i+1):                                # 5432
#         print(end=" ")                                    #  543
#     for j in range(5,i,-1):                               #   54
#         print(j,end="")                                   #    5
#     print()

#  18.pattern ===========================
# for i in range(5,0,-1):                                   #     5
#     for k in range(i,1,-1):                               #    54
#         print(end=" ")                                    #   543
#     for j in range(5,i-1,-1):                             #  5432
#         print(j,end="")                                   # 54321
#     print()

# 19.pattern ===========================
# for i in range(1,6):                                      #     *
#     for k in range(i,5):                                  #    **
#         print(end=" ")                                    #   ***
#     for j in range(1,i+1):                                #  ****
#         print("*",end="")                                 # *****
#     print()

# 20.pattern=============================
# for i in range(1,6):                                      #     1
#     for k in range(i,5):                                  #    22
#         print(end=" ")                                    #   333
#     for j in range(1,i+1):                                #  4444
#         print(i,end="")                                   # 55555
#     print()

# 21.pattern =========================
# for i in range(1,6):                                  #1
#     for j in range(i,0,-1):                           #21
#         print(j,end="")                               #321
#     print()                                           #4321
# for i in range(4,0,-1):                               #54321
#     for j in range(i,0,-1):                           #4321
#         print(j,end="")                               #321
#     print()                                           #21
                                                        #1
# 22.pattern =========================
# for i in range(1,6):                                     #     1
#     for k in range(i,5):                                 #    12
#         print(end=" ")                                   #   123
#     for j in range(1,i+1):                               #  1234
#         print(j,end="")                                  # 12345
#     print()                                              #  2345
# for i in range(2,6):                                     #   345
#     for k in range(1,i):                                 #    45
#         print(end=" ")                                   #     5
#     for j in range(i,6):
#         print(j,end="")
#     print()

# 23.pattern =========================
# for i in range(1,6):                          #1        1
#     for j in range(1,i+1):                    #12      21
#         print(j,end="")                       #123    321
#     for k in range(i,5):                      #1234  4321
#         print(end="  ")                       #1234554321
#     for j in range(i,0,-1):
#         print(j,end="")        
#     print()

# 24.pattern ==========================
# for i in range(5,0,-1):                           #1234554321
#     for j in range(1,i+1):                        #1234  4321
#         print(j,end="")                           #123    321
#     for k in range(4,i-1,-1):                     #12      21
#         print(end="  ")                           #1        1
#     for j in range(i,0,-1):                       #1        1
#         print(j,end="")                           #12      21
#     print()                                       #123    321
# for i in range(1,6):                              #1234  4321
#     for j in range(1,i+1):                        #1234554321
#         print(j,end="")
#     for k in range(i,5):
#         print(end="  ")
#     for j in range(i,0,-1):
#         print(j,end="")        
#     print()

# 25.pattern =========================
# j=1                                               #1
# for i in range(1,6):                              #11
#     print(j,end="")                               #121
#     j=j*11                                        #1331
#     print()                                       #14641

# 26. pattern============================
# p=1                                           #1
# for i in range(1,6):                          #2 3
#     for j in range(1,i+1):                    #4 5 6
#         print(p,end=" ")                      #7 8 9 10
#         p=p+1                                 #11 12 13 14 15
#     print()

# 27.pattern==========================
# for i in range(1,6):                                  #1
#     for j in range(1,i+1):                            #10
#         print(j%2,end="")                             #101
#     print()                                           #1010
                                                        #10101
# 28. pattern =========================
# for i in range(1,6):                                 #*
#     for j in range(1,i+1):                           #*A *
#         if(i==j):                                    #*A *A *
#             print("*",end=" ")                       #*A *A *A *
#         else:                                        #*A *A *A *A *
#             print("*A",end=" ")
#     print()

# 29. pattern ========================
# for i in range(1,6):                                  #     *
#     for k in range(i,5):                              #    * *  
#         print(end=" ")                                #   * * * 
#     for j in range(1,i+1):                            #  * * * * 
#         if(i==j):                                     # * * * * *
#             print("*",end="")                         #  * * * *
#         else:                                         #   * * *  
#             print("* ",end="")                        #    * *
#     print()                                           #     *
# for i in range(1,5):
#         for k in range(1,i+1):
#             print(end=" ")
#         for j in range(4,i-1,-1):
#             if(i==j):
#                 print("*",end="")
#             else:
#                 print("* ",end="")
#         print()

# 30.pattern ===========================
# k=0
# for i in range(1,5):                          #1
#     k=k+i                                     #3 2
#     l=k                                       #6 5 4
#     for j in range(1,i+1):                    #10 9 8 7
#         print(l,end=" ")
#         l-=1
#     print()

# 31.patterm============================
# m=1
# n=1
# for i in range(1,6):                              # 1
#     for j in range(1,i+1):                        # 2 3
#         k=m+n                                     # 5 8 13
#         m=n                                       # 21 34 55 89
#         n=k                                       # 144 233 377 610 987
#         print(m,end=" ")
#     print()

# 32.pattern ============================
# for i in range(1,6):                          #1
#     for j in range(1,i+1):                    #1 3
#         k=j*j-1                               #1 3 8
#         if(k==0):                             #1 3 8 15
#             print(1,end=" ")                  #1 3 8 15 24
#         else:
#             print(k,end=" ")                                              
#     print()
# 33.pattern ===========================
# for i in range(1,11):                         #1
#     for j in range(1,i+1):                    #2 4
#         print(i*j,end=" ")                    #3 6 9
#     print()                                   #4 8 12 16
                                                # 5 10 15 20 25 
                                                # 6 12 18 24 30 36 
                                                # 7 14 21 28 35 42 49 
                                                # 8 16 24 32 40 48 56 64         
                                                # 9 18 27 36 45 54 63 72 81      
                                                # 10 20 30 40 50 60 70 80 90 100 


    #  ===============2nd pattern====================================================
# 1,pattern============================
# for i in range(1,6):      
#     a=1                                       # 1
#     b=0                                       # 1 2
#     for j in range(1,i+1):                    # 1 2 4
#            a=a+b                              # 1 2 4 7
#            print(a,end=" ")                   # 1 2 4 7 11
#            b=b+1              
#     print()

# 2.pattern ==========================
# for i in range(1,6):                          # 1
#     for j in range(1,i+1):                    # 2 4
#         print(i*j,end=" ")                    # 3 6 9
#     print()                                   # 4 8 12 16
                                                # 5 10 15 20 25
# 3.pattern==26 pattern================
# 4.pattern==============================
# for i in range(1,6):                          # 1
#     k=i                                       # 2 4
#     for j in  range(1,i+1):                   # 3 9 27
#         print(k,end=" ")                      # 4 16 64 256
#         k=k*i                                 # 5 25 125 625 3125
#     print()

# 5.pattern=============================
# k=1                                           #1
# for i in range(1,6):                          #8 64
#     for j in range(1,i+1):                    #216 729 1728
#         print(k*k*k, end=" ")                 #3375 6859 12167 19683 
#         k=k+i                                 #29791 46656 68921 97336 132651 
#     print()

# 6.pattern===============================
# k=1                                           
# for i in range(1,6):                          #1
#     for j in range(1,i+1):                    #3 5
#        print(k,end=" ")                       #7 9 11
#        k=k+2                                  #13 15 17 19
#     print()                                   #21 23 25 27 29

# 7.pattern=============================
# for i in range(5,0,-1):                       #5
#     for j in range(5,i-1,-1):                 #44
#         print(i,end="")                       #333
#     print()                                   #2222
                                                #11111












