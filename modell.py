{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b8f3a14f-201d-41c6-9099-48396fb10b57",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "320ef28b-daa6-48b8-a38e-ee701e8fd782",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(r\"C:\\pyythonn\\Assignment 1\\cleaned_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "30f94e8f-872d-4572-bb96-c16e98807da4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>invoice_no</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>category</th>\n",
       "      <th>quantity</th>\n",
       "      <th>price</th>\n",
       "      <th>invoice_date</th>\n",
       "      <th>shopping_mall</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>payment_method</th>\n",
       "      <th>total_sales</th>\n",
       "      <th>age_group</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I138884</td>\n",
       "      <td>C241288</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>5</td>\n",
       "      <td>1500.40</td>\n",
       "      <td>2022-08-05</td>\n",
       "      <td>Kanyon</td>\n",
       "      <td>Female</td>\n",
       "      <td>28.0</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>7502.00</td>\n",
       "      <td>20-29</td>\n",
       "      <td>2022</td>\n",
       "      <td>8</td>\n",
       "      <td>Friday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>I317333</td>\n",
       "      <td>C111565</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>3</td>\n",
       "      <td>1800.51</td>\n",
       "      <td>2021-12-12</td>\n",
       "      <td>Forum Istanbul</td>\n",
       "      <td>Male</td>\n",
       "      <td>21.0</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>5401.53</td>\n",
       "      <td>20-29</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "      <td>Sunday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>I127801</td>\n",
       "      <td>C266599</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>1</td>\n",
       "      <td>300.08</td>\n",
       "      <td>2021-11-09</td>\n",
       "      <td>Metrocity</td>\n",
       "      <td>Male</td>\n",
       "      <td>20.0</td>\n",
       "      <td>Cash</td>\n",
       "      <td>300.08</td>\n",
       "      <td>Teen</td>\n",
       "      <td>2021</td>\n",
       "      <td>11</td>\n",
       "      <td>Tuesday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>I173702</td>\n",
       "      <td>C988172</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>5</td>\n",
       "      <td>3000.85</td>\n",
       "      <td>2021-05-16</td>\n",
       "      <td>Metropol AVM</td>\n",
       "      <td>Female</td>\n",
       "      <td>66.0</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>15004.25</td>\n",
       "      <td>40+</td>\n",
       "      <td>2021</td>\n",
       "      <td>5</td>\n",
       "      <td>Sunday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>I337046</td>\n",
       "      <td>C189076</td>\n",
       "      <td>Books</td>\n",
       "      <td>4</td>\n",
       "      <td>60.60</td>\n",
       "      <td>2021-10-24</td>\n",
       "      <td>Kanyon</td>\n",
       "      <td>Female</td>\n",
       "      <td>53.0</td>\n",
       "      <td>Cash</td>\n",
       "      <td>242.40</td>\n",
       "      <td>40+</td>\n",
       "      <td>2021</td>\n",
       "      <td>10</td>\n",
       "      <td>Sunday</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  invoice_no customer_id  category  quantity    price invoice_date  \\\n",
       "0    I138884     C241288  Clothing         5  1500.40   2022-08-05   \n",
       "1    I317333     C111565     Shoes         3  1800.51   2021-12-12   \n",
       "2    I127801     C266599  Clothing         1   300.08   2021-11-09   \n",
       "3    I173702     C988172     Shoes         5  3000.85   2021-05-16   \n",
       "4    I337046     C189076     Books         4    60.60   2021-10-24   \n",
       "\n",
       "    shopping_mall  gender   age payment_method  total_sales age_group  year  \\\n",
       "0          Kanyon  Female  28.0    Credit Card      7502.00     20-29  2022   \n",
       "1  Forum Istanbul    Male  21.0     Debit Card      5401.53     20-29  2021   \n",
       "2       Metrocity    Male  20.0           Cash       300.08      Teen  2021   \n",
       "3    Metropol AVM  Female  66.0    Credit Card     15004.25       40+  2021   \n",
       "4          Kanyon  Female  53.0           Cash       242.40       40+  2021   \n",
       "\n",
       "   month day_name  \n",
       "0      8   Friday  \n",
       "1     12   Sunday  \n",
       "2     11  Tuesday  \n",
       "3      5   Sunday  \n",
       "4     10   Sunday  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1ecbcd9a-81cb-4c62-b23f-90c0e265d34b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           quantity         price           age   total_sales          year  \\\n",
      "count  99457.000000  99457.000000  99457.000000  99457.000000  99457.000000   \n",
      "mean       3.003429    689.256321     43.425350   2528.789268   2021.629408   \n",
      "std        1.413025    941.184567     14.980437   4222.475781      0.636136   \n",
      "min        1.000000      5.230000     18.000000      5.230000   2021.000000   \n",
      "25%        2.000000     45.450000     30.000000    136.350000   2021.000000   \n",
      "50%        3.000000    203.300000     43.000000    600.170000   2022.000000   \n",
      "75%        4.000000   1200.320000     56.000000   2700.720000   2022.000000   \n",
      "max        5.000000   5250.000000     69.000000  26250.000000   2023.000000   \n",
      "\n",
      "              month  \n",
      "count  99457.000000  \n",
      "mean       6.113898  \n",
      "std        3.569511  \n",
      "min        1.000000  \n",
      "25%        3.000000  \n",
      "50%        6.000000  \n",
      "75%        9.000000  \n",
      "max       12.000000  \n"
     ]
    }
   ],
   "source": [
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a8edcaf9-20ec-4d40-8244-19e9f07647aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(99457, 15)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bf23aaf4-e3ea-499b-9e3c-f7cb83611bd5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "96ca869f-5447-4d8a-bcf1-787cdf9324b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "invoice_no        0\n",
       "customer_id       0\n",
       "category          0\n",
       "quantity          0\n",
       "price             0\n",
       "invoice_date      0\n",
       "shopping_mall     0\n",
       "gender            0\n",
       "age               0\n",
       "payment_method    0\n",
       "total_sales       0\n",
       "age_group         0\n",
       "year              0\n",
       "month             0\n",
       "day_name          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "38e155c3-9cda-4a96-921a-c7394011bf9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(99457, 15)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d384de5f-4248-4e2d-8bad-b0f4e22f0580",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bin edges (Q0, Q1, Q2, Q3, Q4):\n",
      "[5.23000e+00 1.36350e+02 6.00170e+02 2.70072e+03 2.62500e+04]\n",
      "\n",
      "Distribution:\n",
      "spending_category\n",
      "low          25840\n",
      "high         24923\n",
      "medium       24849\n",
      "very_high    23845\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# making a new target column (\"spending_category\")\n",
    "\n",
    "# quantile building\n",
    "spending_bins = pd.qcut(\n",
    "    df[\"total_sales\"],\n",
    "    q=4,\n",
    "    labels=['low', 'medium', 'high', 'very_high']\n",
    ")\n",
    "\n",
    "# range boundaries (edges)\n",
    "quantile_ranges = pd.qcut(\n",
    "    df[\"total_sales\"],\n",
    "    q=4,\n",
    "    retbins=True\n",
    ")\n",
    "\n",
    "# assign the bin as new column\n",
    "df[\"spending_category\"] = spending_bins\n",
    "\n",
    "# show bin ranges\n",
    "print(\"Bin edges (Q0, Q1, Q2, Q3, Q4):\")\n",
    "print(quantile_ranges[1])\n",
    "\n",
    "# distribution check\n",
    "print(\"\\nDistribution:\")\n",
    "print(df[\"spending_category\"].value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ece98caa-7519-426a-9d26-4eed68fc5866",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Target Column: Spending_Category\n",
    "def spending_category(sales):\n",
    "    if sales > 2700:\n",
    "        return \"Very High\"\n",
    "    elif sales > 600:\n",
    "        return \"High\"\n",
    "    elif sales > 135:\n",
    "        return \"Medium\"\n",
    "    else:\n",
    "        return \"Low\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8a8aa33d-628c-46e2-bb83-0ad90e646024",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        very_high\n",
       "1        very_high\n",
       "2           medium\n",
       "3        very_high\n",
       "4           medium\n",
       "           ...    \n",
       "99452       medium\n",
       "99453          low\n",
       "99454          low\n",
       "99455    very_high\n",
       "99456          low\n",
       "Name: spending_category, Length: 99457, dtype: category\n",
       "Categories (4, object): ['low' < 'medium' < 'high' < 'very_high']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"spending_category\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fb092876-bfaf-4436-88ba-23792c630ac0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>invoice_no</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>category</th>\n",
       "      <th>quantity</th>\n",
       "      <th>price</th>\n",
       "      <th>invoice_date</th>\n",
       "      <th>shopping_mall</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>payment_method</th>\n",
       "      <th>total_sales</th>\n",
       "      <th>age_group</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day_name</th>\n",
       "      <th>spending_category</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I138884</td>\n",
       "      <td>C241288</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>5</td>\n",
       "      <td>1500.40</td>\n",
       "      <td>2022-08-05</td>\n",
       "      <td>Kanyon</td>\n",
       "      <td>Female</td>\n",
       "      <td>28.0</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>7502.00</td>\n",
       "      <td>20-29</td>\n",
       "      <td>2022</td>\n",
       "      <td>8</td>\n",
       "      <td>Friday</td>\n",
       "      <td>very_high</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>I317333</td>\n",
       "      <td>C111565</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>3</td>\n",
       "      <td>1800.51</td>\n",
       "      <td>2021-12-12</td>\n",
       "      <td>Forum Istanbul</td>\n",
       "      <td>Male</td>\n",
       "      <td>21.0</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>5401.53</td>\n",
       "      <td>20-29</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "      <td>Sunday</td>\n",
       "      <td>very_high</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>I127801</td>\n",
       "      <td>C266599</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>1</td>\n",
       "      <td>300.08</td>\n",
       "      <td>2021-11-09</td>\n",
       "      <td>Metrocity</td>\n",
       "      <td>Male</td>\n",
       "      <td>20.0</td>\n",
       "      <td>Cash</td>\n",
       "      <td>300.08</td>\n",
       "      <td>Teen</td>\n",
       "      <td>2021</td>\n",
       "      <td>11</td>\n",
       "      <td>Tuesday</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>I173702</td>\n",
       "      <td>C988172</td>\n",
       "      <td>Shoes</td>\n",
       "      <td>5</td>\n",
       "      <td>3000.85</td>\n",
       "      <td>2021-05-16</td>\n",
       "      <td>Metropol AVM</td>\n",
       "      <td>Female</td>\n",
       "      <td>66.0</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>15004.25</td>\n",
       "      <td>40+</td>\n",
       "      <td>2021</td>\n",
       "      <td>5</td>\n",
       "      <td>Sunday</td>\n",
       "      <td>very_high</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>I337046</td>\n",
       "      <td>C189076</td>\n",
       "      <td>Books</td>\n",
       "      <td>4</td>\n",
       "      <td>60.60</td>\n",
       "      <td>2021-10-24</td>\n",
       "      <td>Kanyon</td>\n",
       "      <td>Female</td>\n",
       "      <td>53.0</td>\n",
       "      <td>Cash</td>\n",
       "      <td>242.40</td>\n",
       "      <td>40+</td>\n",
       "      <td>2021</td>\n",
       "      <td>10</td>\n",
       "      <td>Sunday</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  invoice_no customer_id  category  quantity    price invoice_date  \\\n",
       "0    I138884     C241288  Clothing         5  1500.40   2022-08-05   \n",
       "1    I317333     C111565     Shoes         3  1800.51   2021-12-12   \n",
       "2    I127801     C266599  Clothing         1   300.08   2021-11-09   \n",
       "3    I173702     C988172     Shoes         5  3000.85   2021-05-16   \n",
       "4    I337046     C189076     Books         4    60.60   2021-10-24   \n",
       "\n",
       "    shopping_mall  gender   age payment_method  total_sales age_group  year  \\\n",
       "0          Kanyon  Female  28.0    Credit Card      7502.00     20-29  2022   \n",
       "1  Forum Istanbul    Male  21.0     Debit Card      5401.53     20-29  2021   \n",
       "2       Metrocity    Male  20.0           Cash       300.08      Teen  2021   \n",
       "3    Metropol AVM  Female  66.0    Credit Card     15004.25       40+  2021   \n",
       "4          Kanyon  Female  53.0           Cash       242.40       40+  2021   \n",
       "\n",
       "   month day_name spending_category  \n",
       "0      8   Friday         very_high  \n",
       "1     12   Sunday         very_high  \n",
       "2     11  Tuesday            medium  \n",
       "3      5   Sunday         very_high  \n",
       "4     10   Sunday            medium  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "883170ba-d451-456b-88ea-f8157dc0cf2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop unnecessary columns\n",
    "df = df.drop(columns=[\"customer_id\", \"invoice_date\", \"price\", \"quantity\", \"age_group\", \"total_sales\", \"invoice_no\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3fc4401d-4550-48c9-b520-ce48cc98fc74",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['category', 'shopping_mall', 'gender', 'age', 'payment_method', 'year',\n",
       "       'month', 'day_name', 'spending_category'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "715b4eb4-daa7-4887-9f6f-1f9c4d31fd5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "g = sns.pairplot(df, hue=\"spending_category\")\n",
    "#g.savefig(r\"C:\\pyythonn\\Assignment 1\\pairplot.png\", dpi=300, bbox_inches='tight')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "55b21174-38ab-463c-8b27-d18f2d75f4d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.drop(columns=[\"spending_category\"])\n",
    "y = df[\"spending_category\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "35e5e99f-0c58-438d-a15f-c8e54371834b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#splitting data into train 80% and test 20%\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.2, random_state=42, stratify=y\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "598fe364-29d1-4c8d-ae9b-794c226678f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "# Encode target\n",
    "le_target = LabelEncoder()\n",
    "y_train = le_target.fit_transform(y_train)\n",
    "y_test = le_target.transform(y_test)\n",
    "\n",
    "# Day_Name mapping (ordinal)\n",
    "day_map = {\n",
    "    \"Monday\": 1, \"Tuesday\": 2, \"Wednesday\": 3,\n",
    "    \"Thursday\": 4, \"Friday\": 5, \"Saturday\": 6, \"Sunday\": 7\n",
    "}\n",
    "X_train[\"day_name\"] = X_train[\"day_name\"].map(day_map)\n",
    "X_test[\"day_name\"] = X_test[\"day_name\"].map(day_map)\n",
    "\n",
    "# Encode categorical columns in X\n",
    "categorical_cols = [\"gender\", \"payment_method\", \"category\", \"shopping_mall\"]\n",
    "\n",
    "encoders = {}\n",
    "for col in categorical_cols:\n",
    "    le = LabelEncoder()\n",
    "    X_train[col] = le.fit_transform(X_train[col])\n",
    "    X_test[col] = le.transform(X_test[col])   # use same mapping\n",
    "    encoders[col] = le  # store encoder for future use"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c4333e09-3efc-4ba0-9704-e0faa4279053",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>shopping_mall</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>payment_method</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>36744</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>2</td>\n",
       "      <td>2021</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>92004</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>2</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>86146</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>23.0</td>\n",
       "      <td>0</td>\n",
       "      <td>2023</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31576</th>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>22.0</td>\n",
       "      <td>2</td>\n",
       "      <td>2021</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>87726</th>\n",
       "      <td>3</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>44.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2022</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       category  shopping_mall  gender   age  payment_method  year  month  \\\n",
       "36744         3              4       0  27.0               2  2021      7   \n",
       "92004         3              3       1  35.0               2  2021     12   \n",
       "86146         2              4       0  23.0               0  2023      2   \n",
       "31576         1              7       0  22.0               2  2021      3   \n",
       "87726         3              6       1  44.0               1  2022      6   \n",
       "\n",
       "       day_name  \n",
       "36744         1  \n",
       "92004         3  \n",
       "86146         2  \n",
       "31576         5  \n",
       "87726         4  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d11b9add-9642-4ce8-8685-2f99a6f2a586",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1, 1, ..., 2, 2, 3], shape=(79565,))"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f26c177c-8162-4e7f-a9c3-c6a6b5db7597",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "# Select only numerical columns (confirm they exist in your dataset)\n",
    "num_cols = [\"age\", \"year\", \"month\"]\n",
    "\n",
    "scaler = StandardScaler()\n",
    "\n",
    "# Make copies\n",
    "X_train_scaled = X_train.copy()\n",
    "X_test_scaled = X_test.copy()\n",
    "\n",
    "# Fit on training, transform both\n",
    "X_train_scaled[num_cols] = scaler.fit_transform(X_train[num_cols])\n",
    "X_test_scaled[num_cols] = scaler.transform(X_test[num_cols])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2a07a013-8c5b-45be-b424-3d1e45d8b060",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>shopping_mall</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>payment_method</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>36744</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>-1.096013</td>\n",
       "      <td>2</td>\n",
       "      <td>-0.991708</td>\n",
       "      <td>0.249890</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>92004</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.561798</td>\n",
       "      <td>2</td>\n",
       "      <td>-0.991708</td>\n",
       "      <td>1.649512</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>86146</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>-1.363121</td>\n",
       "      <td>0</td>\n",
       "      <td>2.154497</td>\n",
       "      <td>-1.149733</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31576</th>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>-1.429898</td>\n",
       "      <td>2</td>\n",
       "      <td>-0.991708</td>\n",
       "      <td>-0.869808</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>87726</th>\n",
       "      <td>3</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>0.039193</td>\n",
       "      <td>1</td>\n",
       "      <td>0.581395</td>\n",
       "      <td>-0.030035</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1496</th>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>-0.762129</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.991708</td>\n",
       "      <td>-0.030035</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>68702</th>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>1.040846</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.991708</td>\n",
       "      <td>0.249890</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36289</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>-1.029236</td>\n",
       "      <td>0</td>\n",
       "      <td>0.581395</td>\n",
       "      <td>1.369588</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43261</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.027584</td>\n",
       "      <td>0</td>\n",
       "      <td>-0.991708</td>\n",
       "      <td>0.809739</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16364</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>-1.630228</td>\n",
       "      <td>0</td>\n",
       "      <td>0.581395</td>\n",
       "      <td>-0.030035</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>79565 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       category  shopping_mall  gender       age  payment_method      year  \\\n",
       "36744         3              4       0 -1.096013               2 -0.991708   \n",
       "92004         3              3       1 -0.561798               2 -0.991708   \n",
       "86146         2              4       0 -1.363121               0  2.154497   \n",
       "31576         1              7       0 -1.429898               2 -0.991708   \n",
       "87726         3              6       1  0.039193               1  0.581395   \n",
       "...         ...            ...     ...       ...             ...       ...   \n",
       "1496          1              5       0 -0.762129               1 -0.991708   \n",
       "68702         1              7       0  1.040846               1 -0.991708   \n",
       "36289         0              3       1 -1.029236               0  0.581395   \n",
       "43261         1              1       1 -0.027584               0 -0.991708   \n",
       "16364         1              2       0 -1.630228               0  0.581395   \n",
       "\n",
       "          month  day_name  \n",
       "36744  0.249890         1  \n",
       "92004  1.649512         3  \n",
       "86146 -1.149733         2  \n",
       "31576 -0.869808         5  \n",
       "87726 -0.030035         4  \n",
       "...         ...       ...  \n",
       "1496  -0.030035         1  \n",
       "68702  0.249890         5  \n",
       "36289  1.369588         1  \n",
       "43261  0.809739         1  \n",
       "16364 -0.030035         4  \n",
       "\n",
       "[79565 rows x 8 columns]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_scaled"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "42127fac-7cb3-4674-9cff-a52b659834a9",
   "metadata": {},
   "outputs": [],
   "source": [
    " #Logistic Regression model\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "log_reg = LogisticRegression(max_iter=1000, random_state=42)\n",
    "\n",
    "# Train\n",
    "log_reg.fit(X_train_scaled, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred = log_reg.predict(X_test_scaled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "da6c93ed-3c61-45d8-b470-c0ae4a52bad5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.5011562437160667\n"
     ]
    }
   ],
   "source": [
    "# Decision Tree model\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "dt = DecisionTreeClassifier(random_state=42, max_depth=None)  # max_depth=None means pura tree grow karega\n",
    "dt.fit(X_train_scaled, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred_dt = dt.predict(X_test_scaled)\n",
    "\n",
    "# Accuracy\n",
    "acc = accuracy_score(y_test, y_pred_dt)\n",
    "print(\"Accuracy:\", acc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "19a52c10-13a6-4fdb-b6cf-36950ae1e344",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.5458978483812588\n"
     ]
    }
   ],
   "source": [
    "# Random Forest model\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "rf_model = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=42)\n",
    "\n",
    "# Train\n",
    "rf_model.fit(X_train_scaled, y_train)\n",
    "\n",
    "# Predict\n",
    "y_pred_rf = rf_model.predict(X_test_scaled)\n",
    "\n",
    "# Accuracy\n",
    "acc = accuracy_score(y_test, y_pred_rf)\n",
    "print(\"Accuracy:\", acc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "637a4bc4-9e67-4cc1-b7c1-a3a6672a37d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.5019103157048059\n"
     ]
    }
   ],
   "source": [
    "# KNN model\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "knn = KNeighborsClassifier(n_neighbors=5)\n",
    "\n",
    "#Train\n",
    "knn.fit(X_train_scaled, y_train)\n",
    "\n",
    "#Predict on test set\n",
    "y_pred_knn = knn.predict(X_test_scaled)\n",
    "\n",
    "# Accuracy\n",
    "acc = accuracy_score(y_test, y_pred_knn)\n",
    "print(\"Accuracy:\", acc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5df0d8fa-f132-4536-b14c-6f7b61de876a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "done\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score\n",
    "\n",
    "# Function to evaluate models\n",
    "def evaluate_model(y_true, y_pred, model_name):\n",
    "    return {\n",
    "        \"Model\": model_name,\n",
    "        \"Accuracy\": accuracy_score(y_true, y_pred),\n",
    "        \"Precision\": precision_score(y_true, y_pred, average=\"weighted\"),\n",
    "        \"Recall\": recall_score(y_true, y_pred, average=\"weighted\"),\n",
    "        \"F1-score\": f1_score(y_true, y_pred, average=\"weighted\")\n",
    "    }\n",
    "\n",
    "# Collect all results\n",
    "results = []\n",
    "print(\"done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5b529ceb-531b-41f8-8bea-13c660bbf708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 Model  Accuracy  Precision    Recall  F1-score\n",
      "0  Logistic Regression  0.428313   0.336615  0.428313  0.356924\n",
      "1        Decision Tree  0.501156   0.501286  0.501156  0.501181\n",
      "2        Random Forest  0.545898   0.547830  0.545898  0.545469\n",
      "3                  KNN  0.501910   0.510082  0.501910  0.502859\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\St.law\\miniconda3\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1731: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", result.shape[0])\n"
     ]
    }
   ],
   "source": [
    "results.append(evaluate_model(y_test, y_pred, \"Logistic Regression\"))\n",
    "results.append(evaluate_model(y_test, y_pred_dt, \"Decision Tree\"))\n",
    "results.append(evaluate_model(y_test, y_pred_rf, \"Random Forest\"))\n",
    "results.append(evaluate_model(y_test, y_pred_knn, \"KNN\"))\n",
    "\n",
    "# Convert to DataFrame for clean table\n",
    "results_df = pd.DataFrame(results)\n",
    "\n",
    "print(results_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "89593041-1fc0-43ba-af90-65dabb996d44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAArMAAAIwCAYAAACVw+NtAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjMsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvZiW1igAAAAlwSFlzAAAPYQAAD2EBqD+naQAAVz5JREFUeJzt3QmYzeX7x/HbvlWWbJHshZQ1a5JSlIgotBBSKVGqX2mhqCxJEiGRSpgW7cUvShtlSxQqbbZsLUg1xPlfn+d/fc/vzCbLmTnnmfN+XdfEnDkzvjPz7ZzPub/3cz85QqFQyAAAAAAP5Yz1AQAAAABHijALAAAAbxFmAQAA4C3CLAAAALxFmAUAAIC3CLMAAADwFmEWAAAA3iLMAgAAwFuEWQAAAHiLMAsgU+TIkcPuu+++w/68H3/80X3utGnTMuW4spsKFSrY1VdfbfHswgsvtN69e8f6MLw1ceJEO+mkkyw5OTnWhwLEJcIskI0pECoY6u3jjz9O83HtZl2uXDn38Ysuush8tHXrVrvtttusWrVqVrBgQStUqJDVq1fPHnjgAfv9999jfXgJ75NPPrH//ve/dscdd6T78bffftudf2XKlLEDBw5k+fH5QC9W9u7da5MmTYr1oQBxKXesDwBA5sufP7/NmDHDzjzzzBS3f/DBB7Zx40bLly+f+WjJkiWu6vfHH3/YlVde6UKsLF261IYPH24ffvihC1LZ2ddff205c8ZvXeLhhx+2c88916pUqZLux59//nlXXVZF/r333rOWLVtm+TH68P9v9+7dbfTo0XbTTTe58A/gf+L3ERBA1Cjwvfjii/bPP/+kuF0BVwGwdOnS5htVXTt06GC5cuWyzz//3CZPnmzXX3+9e3vqqafsu+++s7POOsuyI1XU//rrL/d3vRDJkyePxaNt27bZW2+9ZZdddlm6H9+zZ4+99tprNmDAAKtTp44LtvFKxxpL+hn+9NNP9v7778f0OIB4RJgFEkDXrl3tl19+sXfffTd8my5bvvTSS3b55Zdn+OR96623ujYEBaZTTjnFRo0a5YJUJPXx3XLLLVaiRAk79thjrV27dq7am55NmzZZz549rVSpUu5rnnrqqTZ16tQj+p50yVVfT9UqtRikpn/jnnvuSXHbE0884f5N/du6rH3jjTemaUU4++yzrWbNmrZy5Upr3ry5a11QVVE/q6Ca3bBhQytQoID7mcybNy/F56tPWJWztWvXugBy3HHH2fHHH2/9+/e3v//+O8V9n376aTvnnHOsZMmS7phq1KhhEyZMSPO9qHKpNpC5c+da/fr13b8dXHJO3TO7b98+u//++61q1aquoqd/WxX5yN+9qArarFkz15ZRpEgRu/jii23NmjXpfi/r1q1z/4buV7hwYevRo4f9+eef//o7UpDVC6iMqq2vvPKKC+WXXnqpdenSxWbPnp3mZyS6Tcdy8sknu+/phBNOsEsuucS9YAmoReGxxx6z0047zd1H52Pr1q1dlf7ferFT93cH3/fq1avd/x9FixYNX9XQeaGfRaVKldy/oxeCOqf1/1dqOj979erlzjX9fitWrGh9+vRx/+99//337t949NFH03zewoUL3cdmzpwZvk0vOosVK+bCP4CUCLNAAlDgady4cYonx3feecd27tzpQkRqCqwKpXqiVSBQYFRwu/32210VLdI111xjY8aMsfPPP99d2leVsE2bNun2tjZq1MiFv759+7rgoZCoJ3t9/uF6/fXXXajr1KnTId1fAUXhVcHikUcesY4dO7pAqONWAIz022+/ufCo0Dpy5EgXRPRzSkpKcn+q0q3vVYFf//7u3bvT/HsKsgphw4YNc/cfO3asXXvttSnuo+Bavnx5u+uuu9wx6YXDDTfcYOPHj0+3nUAvSs477zz3s6tdu3aG36fCbIsWLWzcuHF29913u8VDy5cvD99Hv4NWrVq5yqnur9+pAlTTpk1d6Evve9H3qO9Ff1cg1L/xb/Q1Fab1PaZHlVgdpwKhfq76N954440U99m/f7/7XejfU6DTz0kvDHTufvnll+H76Ty6+eab3c9wxIgRduedd7qw+emnn9qRUshWaH/ooYfCC9j0okBBVIH+8ccfd8c9a9Ys9zuOfKG3efNma9CggftY586d3e//qquuci+G9DUVhvXzTq8ardv0wlAvMCLVrVvX9SADSCUEINt6+umn9ewaWrJkSWjcuHGhY489NvTnn3+6j1166aWhFi1auL+XL18+1KZNm/Dnvfrqq+7zHnjggRRfr1OnTqEcOXKE1q1b595fsWKFu98NN9yQ4n6XX365u33w4MHh23r16hU64YQTQjt27Ehx3y5duoQKFy4cPq4ffvjBfa6O/WCKFi0aqlWr1iH9HLZt2xbKmzdv6Pzz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AAB4izALAAAAbxFmAQAA4C3CLAAAALxFmAUAAIC3CLMAAADwFmEWAAAA3iLMAgAAwFuEWQAAAHiLMAsAAABvEWYBAADgLcIsAAAAvEWYBQAAgLcIswAAAPAWYRYAAADeIswCAADAW4RZAAAAeIswCwAAAG8RZgEAAOAtwiwAAAC8RZgFAACAtwizAAAASJwwW6FCBRsyZIitX78+c44IAAAAyKwwe/PNN9vs2bOtUqVKdt5559msWbMsOTn5cL8MAAAAEJswu2LFClu8eLFVr17dbrrpJjvhhBOsb9++tnz58qM/IgAAACCze2br1q1rY8eOtc2bN9vgwYPtqaeesjPOOMNq165tU6dOtVAodKRfGgAAADgkue0I7du3z1555RV7+umn7d1337VGjRpZr169bOPGjXbXXXfZvHnzbMaMGUf65QEAAIDoh1m1EijAzpw503LmzGndunWzRx991KpVqxa+T4cOHVyVFgAAAIirMKuQqoVfEyZMsPbt21uePHnS3KdixYrWpUuXaB0jAAAAEJ0w+/3331v58uUPep9ChQq56i0AAAAQVwvAtm3bZp999lma23Xb0qVLo3VcAAAAQPTD7I033mgbNmxIc/umTZvcxwAAAIC4DbOrV692Y7lSq1OnjvsYAAAAELdhNl++fLZ169Y0t//888+WO/cRT/oCAAAAMj/Mnn/++TZw4EDbuXNn+Lbff//dzZbVlAMAAAAgqxx2KXXUqFF21llnuYkGai0QbW9bqlQpe+655zLjGAEAAIDohNmyZcvaypUr7fnnn7cvvvjCChQoYD169LCuXbumO3MWAAAAiJs2g2CO7LXXXmvjx493lVrtAnY0QVZfp0KFCpY/f35r2LChLV68OMP7zp492+rXr29FihRxx1G7dm0qwgAAAAnqiFdsaXLB+vXrbe/evSlub9eu3WF9naSkJBswYIBNnDjRBdkxY8ZYq1at7Ouvv7aSJUumuX+xYsXs7rvvdtvn5s2b1958801XGdZ99XkAAABIHEe0A1iHDh1s1apVliNHDguFQu52/V32799/WF9v9OjR1rt3bxdIRaH2rbfesqlTp9qdd96Z5v5nn312ivf79+9vzzzzjH388ceEWQAAgARz2G0GCo8VK1Z0O4EVLFjQvvrqK/vwww/dpf8FCxYc1tdSVXfZsmXWsmXL/x1Qzpzu/UWL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arr3T05Odm+BnTt3uj937dp1xMe9P/mvI/5c+OdozpWjxbmWWDjXkFU41xDv51rweaFQKL7D7I4dO2z//v1WqlSpFLfr/bVr16b7OVu2bEn3/ro9PcOGDbP7778/ze3lypU7qmNH4ij8+PWxPgQkCM41ZBXONfhyru3evdsKFy4cv2E2K6jqG1nJPXDggP366692/PHHW44cOWJ6bD7RKyS9ANiwYYMdd9xxsT4cZGOca8gqnGvIKpxrh08VWQXZMmXK/Ot9Yxpmixcvbrly5bKtW7emuF3vly5dOt3P0e2Hc/98+fK5t0hFihQ56mNPVPqfkP8RkRU415BVONeQVTjXDs+/VWTjYgFY3rx5rV69ejZ//vwUlVO937hx43Q/R7dH3l/efffdDO8PAACA7CvmbQZqAejevbvVr1/fGjRoYGPGjLE9e/a46QbSrVs3K1u2rOt9lf79+1vz5s3tkUcesTZt2tisWbNs6dKl9uSTT8b4OwEAAEDChdnOnTvb9u3bbdCgQW4RV+3atW3OnDnhRV7r1693Ew4CTZo0sRkzZtg999xjd911l1WtWtVNMqhZs2YMv4vsT60amgWcumUDiDbONWQVzjVkFc61zJUjdCgzDwAAAIA4FPNNEwAAAIAjRZgFAACAtwizAAAA8BZhFgAAAN4izAIAAMBbhFlkSwzpABCPtDFQatqyE4mL56ujR5hFtnyCyJEjR8yOBX49gezfv9/+/vvvWB8OEoTmpv/0009ugyB58cUX3eZAO3fujPWhIQv9/PPP9u2337q/83yVDTZNAKIRSoKNNSZPnmxfffWVnXjiiXbRRRdZtWrVYn14iNNzRk8gb7/9ttuEZcWKFda+fXtr2LChtW3bNtaHh2zsn3/+sQkTJtg777xjn3/+uT333HM2derUQ96DHv7Ti+ezzz7bTj75ZBs1apSdcsopsT4k77FpAryvyAZBduDAgfbUU0/Z6aefbr/88osLK3rSaNSoUawPE3Ho9ddft65du9ott9xilSpVsmnTprndCGfOnOl2IgQyy19//eV2v3zzzTftsssuc9uyB1cJcuXKFevDQxb44IMP3ONPixYt7N5776XwcpRoM4DXgiCryzW7du2yuXPn2vz58238+PHuVe+VV15pn376aawPE3Fmx44driLy0EMP2QMPPGCXX365rVmzxi688EKCLDJNUDvKmzevFSlSxM477zzbuHGjDRs2zN2uIKtAi+xdgNFb8+bN7aWXXrL//ve/NnToUFu7dm2sD81rhFl4Tz1nelJYsmSJay+Qpk2b2u23325169a1q666ikCLFPLnz29//vmntWnTxn744QerUqWKdejQwR555BH38Xnz5rnbgWi3tixbtsw2bdpkzzzzjCUlJVmdOnXstddeSxFogxdcyD42bNhgq1evdm0mQRGmSZMm9vLLL7tAe//99xNojwJhFt7TA4N6jvRA8Pvvv4dvr1+/vv3nP/9xfyrsqpcWiSuoiulPLbbRpd5PPvnEzj//fLvgggtcS4p8//33rocxWJwBRCvIvvLKK676//jjj7tWKFVn7777bjvjjDNc24uuFMigQYOsT58+lpycHOtDRxSo+l6xYkWrWbOmXXHFFXbjjTe6Aovams4666zwFUVdJeJ56gipZxbwxf79+9O9fe7cuaHGjRuHzjjjjNCaNWtSfOyTTz4J3XvvvaF//vkni44S8eTAgQPuz7/++sv9GZwHd999dyhHjhyhdu3apbj/XXfdFTrttNNC69evj8HRIrt6++23QwUKFAhNmTIltH379hQf27p1a+i2224LVa5cOVS9evVQsWLFQp9++mnMjhXRfexZtWqVe37S483AgQNDTZs2DVWtWjVUqlSpUP/+/UP//e9/Q2+++WaoaNGioZtuuim0YsWKWB+6d1gABi8Xe6l5XlULXbJRpSO4NPzwww+7mY1PP/10uitEWWCRmBUxXcabMmWKOzcKFCjgeqpz587tKvfPP/+865/dt2+ffffdd251+UcffWS1atWK9eEjm9i7d69de+21VrJkSRs5cqTt2bPH1q9fb9OnT3cVO7W7HHvssbZo0SL7+uuvrXXr1q71Bf5PLVBLkx5b1JN/3XXXueex999/33799VfXIqcKraaqaLqBKrR6Tuvbt697TFJvNQ4NYRbeUS+sxinpQUKz+nSZRv1m6j1TaBk9erR7spg4caKdeuqpsT5cxJj6EbXAS1MLFBDGjRtnW7Zssc8++8yFXU3AeOGFF1yYqFChgltZrMuBQLQozKjVSWFWLQY6x9TGsnnzZtfy0qVLl/DcWWQPeozRmg1NR9FiL4VUBVpNsdAL6gULFrjHHN2uYKsX0B9++KH7Uy9yatSoEetvwS+xLg0Dh+PJJ58MlShR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sGCB5ciRw37//fdD/pwKFSrYmDFjMvW4ACCaCLMAECNXX321C5vXX399mo/deOON7mO6DwAgY4RZAIihcuXK2axZs+yvv/4K3/b333/bjBkz7KSTTorpsQGADwizABBDdevWdYF29uzZ4dv0dwXZOnXqhG9LTk62fv36WcmSJS1//vx25pln2pIlS1J8rbfffttOPvlkK1CggLVo0cJ+/PHHNP/exx9/bM2aNXP30b+rr7lnz55M/i4BIPMQZgEgxnr27GlPP/10+P2pU6dajx49UtznP//5j7388sv2zDPP2PLly61KlSrWqlUr+/XXX93HN2zYYJdccom1bdvWVqxYYddcc43deeedKb7Gd999Z61bt7aOHTvaypUrLSkpyYXbvn37ZtF3CgDRR5gFgBi78sorXaj86aef3Nsnn3zibguocjphwgR7+OGH7YILLrAaNWrY5MmTXXV1ypQp7j76eOXKle2RRx6xU045xa644oo0/bbDhg1zt998881WtWpVa9KkiY0dO9aeffZZ19oAAD7KHesDAIBEV6JECWvTpo1NmzbNQqGQ+3vx4sVTVFT37dtnTZs2Dd+WJ08ea9Cgga1Zs8a9rz8bNmyY4us2btw4xftffPGFq8g+//zz4dv07x04cMB++OEHq169eiZ+lwCQOQizABAnrQbB5f7x48dnyr/xxx9/2HXXXef6ZFNjsRkAXxFmASAOqJd17969bhyXemEjqX0gb968rv2gfPny7jZVarUATC0Doqrq66+/nuLzPv300zSLzVavXu36bQEgu6BnFgDiQK5cuVyrgMKm/h6pUKFC1qdPH7v99tttzpw57j69e/e2P//803r16uXuo1m13377rbvP119/7UZ7qW0h0h133GELFy50FWAtEtP9X3vtNRaAAfAaYRYA4sRxxx3n3tIzfPhwN4XgqquuchXWdevW2dy5c61o0aLhNgFNO3j11VetVq1aNnHiRHvooYdSfI3TTz/dPvjgA/vmm2/ceC6N/ho0aJCVKVMmS74/AMgMOULq/gcAAAA8RGUWAAAA3iLMAgAAwFuEWQAAAHiLMAsAAABvEWYBAADgLcIsAAAAvEWYBQAAgLcIswAAAPAWYRYAAADeIswCAADAW4RZAAAAmK/+DxhTikt4RMr+AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 800x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Optional: Visualization\n",
    "plt.figure(figsize=(8,5))\n",
    "sns.barplot(x=\"Model\", y=\"Accuracy\", data=results_df)\n",
    "plt.title(\"Model Comparison (Accuracy)\")\n",
    "plt.ylabel(\"Accuracy\")\n",
    "plt.xticks(rotation=45)\n",
    "plt.savefig(r\"C:\\pyythonn\\Assignment 1\\barplot.png\", dpi=300, bbox_inches='tight')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "87fbc5a6-e25c-4fe8-91ad-899cb90a8598",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 600x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report (Random Forest - Default):\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "        high       0.39      0.38      0.39      4985\n",
      "         low       0.81      0.76      0.79      5168\n",
      "      medium       0.44      0.41      0.42      4970\n",
      "   very_high       0.53      0.63      0.58      4769\n",
      "\n",
      "    accuracy                           0.55     19892\n",
      "   macro avg       0.55      0.54      0.54     19892\n",
      "weighted avg       0.55      0.55      0.55     19892\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix, classification_report\n",
    "\n",
    "y_pred_rf = rf_model.predict(X_test_scaled)\n",
    "\n",
    "# Confusion Matrix\n",
    "cm = confusion_matrix(y_test, y_pred_rf)\n",
    "\n",
    "plt.figure(figsize=(6,4))\n",
    "sns.heatmap(cm, annot=True, fmt=\"d\", cmap=\"Blues\",\n",
    "            xticklabels=le_target.classes_, \n",
    "            yticklabels=le_target.classes_)\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.ylabel(\"Actual\")\n",
    "plt.title(\"Confusion Matrix - Random Forest (Default)\")\n",
    "plt.savefig(r\"C:\\pyythonn\\Assignment 1\\heatmap.png\", dpi=300, bbox_inches='tight')\n",
    "plt.show()\n",
    "\n",
    "#  Classification Report\n",
    "print(\"Classification Report (Random Forest - Default):\\n\")\n",
    "print(classification_report(y_test, y_pred_rf, target_names=le_target.classes_))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c958a5c1-4dec-4efd-a98e-62f792260170",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
