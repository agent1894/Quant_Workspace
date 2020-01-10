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
            int length;
            void calculate()
            {
                double sum = 0.0;
                double min = sales[0];
                double max = sales[0];
                double average = 0.0;
                for (int i = 0; i < ((length < QUARTERS) ? length : QUARTERS); i++)
                {
                    sum += sales[i];
                    min = (min < sales[i]) ? min : sales[i];
                    max = (max > sales[i]) ? max : sales[i];
                    if (length != 0)
                        average = sum / length;
                }
            }
        public:
            Sales()
            {
                length = 4;
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