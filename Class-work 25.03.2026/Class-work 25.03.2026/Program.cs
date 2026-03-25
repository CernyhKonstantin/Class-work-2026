using System;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

class Program
{
    static async Task<double> GetUsdRate()
    {
        Console.WriteLine("Requesting USD exchange rate...");

        using (HttpClient client = new HttpClient())
        {
            string url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json";

            string json = await client.GetStringAsync(url);

            Console.WriteLine("Data received, searching for USD rate...");

            await Task.Delay(500);

            string[] parts = json.Split('{');

            foreach (var part in parts)
            {
                if (part.Contains("\"cc\":\"USD\""))
                {
                    int index = part.IndexOf("\"rate\":");
                    string ratePart = part.Substring(index + 7);

                    int end = ratePart.IndexOf(",");
                    string rateString = ratePart.Substring(0, end);

                    double rate = double.Parse(rateString.Replace(".", ","));

                    Console.WriteLine($"USD rate found: {rate}");
                    return rate;
                }
            }
        }

        return 0;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Enter amount in UAH:");
        double uah = double.Parse(Console.ReadLine());

        var rateTask = GetUsdRate();

        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine("Main thread is working...");
            Thread.Sleep(300);
        }

        rateTask.Wait();

        double usdRate = rateTask.Result;

        double usd = uah / usdRate;

        Console.WriteLine($"\nConverted amount: {usd:F2} USD");
    }
}