// 10.10.4 -- re-write 9.6.4 namespace
#ifndef SALES_H_
#define SALES_H_
namespace SALES
{
    class Sales
    {
        private:
            static const int QUARTERS = 4;
            double sales[QUARTERS];
            double sum;
            double min;
            double max;
            double average;
            void calculate()
            {
                sum = 0.0;
                min = sales[0];
                max = sales[0];
                average = 0.0;
                for (int i = 0; i < QUARTERS; i++)
                {
                    sum += sales[i];
                    min = (min < sales[i]) ? min : sales[i];
                    max = (max > sales[i]) ? max : sales[i];
                    average = sum / QUARTERS;
                }
            }
        public:
            Sales()
            {
                for (int i = 0; i < QUARTERS; i++)
                {
                    sales[i] = 0.0;
                }
                calculate();
            }
            Sales(const double ar[], int n);
            void setSales();
            void showSales() const;
    };
}

#endif