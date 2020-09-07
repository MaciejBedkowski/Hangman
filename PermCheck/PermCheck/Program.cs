using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace PermCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] A = { 4,1,3,2};
            int permNumber = 0;
            int check = 1;

            for (int i = 0; i<A.Length; i++)
            {
                if(A[i]==check)
                {
                    check++;
                    WriteLine("Table:" + A[i]);
                    i = -1;
                    
                    WriteLine("Check:"+check);
                    WriteLine(i);
                }
            }
            if(check == A.Length+1)
            {
                permNumber = 1;
            }
            
            ReadKey();
        }
    }
}
