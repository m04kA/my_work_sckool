﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace Coder
{
    class Program
    {
        static void Main(string[] args)
        {
            char[] alphabet = new char[] { 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',  'g', 'G',  'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O',  'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z' }; //Алфавит.

            Console.WriteLine("Введите слово, которое хотите закодировать на английском языке:");
            string words = Console.ReadLine(); //Строчка ввода слова.
            #region Для тестов без участия ввода в консоль.
            //string words = "a aab"; 
            //Console.WriteLine(words);
            #endregion

            char[] arrayWords = words.ToCharArray(); // .ToLower() - Для возведения в нижний регистр.

            Console.WriteLine("Введите код для шифрования сообщения:");
            string code = Console.ReadLine(); //Строчка ввода лозунга.
            #region Для тестов без участия ввода в консоль.
            //string code = "123";
            //Console.WriteLine(code);
            #endregion
            char[] cipher = code.ToCharArray();
            var numbers = new List<int>();

            int figure = 0;
            string a; // Для того, чтоб нормально положить значение в лист, не знаю, как сделать правильней.(Пробовал, не получилось) 
            string finishWord = ""; //То, что получилось в итоге.

            for (int i = 0; i < cipher.Length; i++) // Заполнение листа.
            {
                a = Convert.ToString(cipher[i]);
                figure = (Int32.Parse(a)) * 2; // Умножение на 2, т.к. с добавлением в массив алфовита больших букв, он(массив алфовита) расширился в 2 раза.
                numbers.Add(figure);
            }

            int count = numbers.Count; // Количество элементов в листе.  
            int amount = (alphabet.Length) - 1; // Длинна массива алфовита.


                int m = 0; //Индекс массива arrayWords  
                int n = 0; //Индекс массива alphabet
                int t = 0; // Индекс лозунга.
                int crossing = 0; // Для перехода из конца алфавита в начало. 
                char gap = ' '; // Будет использоваться, для проверки на пробел.
                char question = '?'; // Будет использоваться, для проверки на знаки припинания "?"
                char exclamation_mark = '!'; // Будет использоваться, для проверки на знаки припинания "!"
                char point = '.'; // Будет использоваться, для проверки на знаки припинания "."
                char comma = ','; // Будет использоваться, для проверки на знаки припинания ","
                char colon = ':'; // Будет использоваться, для проверки на знаки припинания ":"
                char semicolon = ';'; // Будет использоваться, для проверки на знаки припинания ":"

            do
            {
                     if(arrayWords[m] == gap)  //Проверка на знаки препинания.
                     {
                        ++m;
                        finishWord = finishWord + gap;
                        
                     } 

                    else
                    {
                        if (arrayWords[m] == question)  //Проверка на знаки препинания.
                    {
                            ++m;
                            finishWord = finishWord + question;

                        }

                        else
                        {
                            if (arrayWords[m] == exclamation_mark)  //Проверка на знаки препинания.
                        {
                            ++m;
                                finishWord = finishWord + exclamation_mark;

                            }
                            else
                            {
                                if (arrayWords[m] == point)  //Проверка на знаки препинания.
                            {
                                    ++m;
                                    finishWord = finishWord + point;

                                }
                                else
                                {
                                    if (arrayWords[m] == comma)  //Проверка на знаки препинания.
                                {
                                        ++m;
                                        finishWord = finishWord + comma;

                                    }
                                    else
                                    {
                                        if (arrayWords[m] == colon)  //Проверка на знаки препинания.
                                    {
                                            ++m;
                                            finishWord = finishWord + colon;

                                        }
                                        else
                                        {
                                            if (arrayWords[m] == semicolon)  //Проверка на знаки препинания.
                                        {
                                                ++m;
                                                finishWord = finishWord + semicolon;

                                            }
                                            else
                                            {
                                                if (t > (count - 1)) // Обновление лозунга
                                                {
                                                    t = 0;
                                                }

                                                if (arrayWords[m] == alphabet[n])  // Сравнение слова с алфовитом
                                                {
                                                    if ((n + numbers[t]) > amount) // Преход с конца алфовита в начало.
                                                    {
                                                        crossing = (numbers[t] - 1) - (amount - n); //numbers[m] - 1 делается потому, что индексы в массиве алфовита начинаются с нуля. 
                                                        finishWord = finishWord + alphabet[crossing];
                                                        ++m;
                                                        n = 0;
                                                        ++t;

                                                    }
                                                    else // Без каких либо проблем.
                                                    {
                                                        finishWord = finishWord + alphabet[n + numbers[t]];
                                                        ++m;
                                                        n = 0;
                                                        ++t;
                                                    }
                                                }
                                                else
                                                {
                                                    ++n;
                                                }

                                            }


                                            

                                        }

                                        

                                    }

                                    

                                }

                                

                            }

                            

                        }
                        

                    }

                     
                    
                        
                    
            } while (m < arrayWords.Length);

            Console.WriteLine($"Результат кодировки: {finishWord}");
            #region Для тестов нижнего блока.
            /*int[] n = new int[] {0, 1};
            int i = 0;          
            do
            {
                if (n[i] >= 3)
                {
                    Console.WriteLine("Молодец!");
                    ++i;
                    //break;
                }
                else
                {
                    n[i]++;
                }
                Console.WriteLine("test");
            } while (i < n.Length);

            Console.WriteLine("test 2");*/

            #endregion


            Console.ReadKey();

        }
    }
}
