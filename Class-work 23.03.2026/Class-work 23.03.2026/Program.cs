using System;
using System.Collections.Concurrent;
using System.Threading;

class Order
{
    public int Id { get; set; }
    public string ProductName { get; set; }
}

class Program
{
    static ConcurrentQueue<Order> orderQueue = new ConcurrentQueue<Order>();
    static bool isRunning = true;

    static void ProcessOrders(object obj)
    {
        while (isRunning || !orderQueue.IsEmpty)
        {
            if (orderQueue.TryDequeue(out Order order))
            {
                Console.WriteLine(
                    $"Worker {Thread.CurrentThread.ManagedThreadId} is processing Order {order.Id}: {order.ProductName}"
                );

                Thread.Sleep(500);

                Console.WriteLine(
                    $"Order #{order.Id} for product {order.ProductName} has been completed"
                );
            }
            else
            {
                Thread.Sleep(100);
            }
        }
    }

    static void Main()
    {
        Console.WriteLine("Worker system is running...");

        Thread[] workers = new Thread[3];

        for (int i = 0; i < workers.Length; i++)
        {
            workers[i] = new Thread(ProcessOrders);
            workers[i].Start();
        }

        int orderId = 1;

        while (true)
        {
            Console.WriteLine("Enter product name (or 'exit' to stop):");
            string input = Console.ReadLine();

            if (input.ToLower() == "exit")
            {
                break;
            }

            Order newOrder = new Order
            {
                Id = orderId++,
                ProductName = input
            };

            orderQueue.Enqueue(newOrder);
            Console.WriteLine("Order pushed to queue");
        }

        isRunning = false;

        foreach (var worker in workers)
        {
            worker.Join();
        }

        Console.WriteLine("All workers finished.");
    }
}