{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "35f8bc1f-882d-49c9-b999-c57fb03a78c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9549b55-cab3-4f47-abf0-12fbfe8f6e7c",
   "metadata": {},
   "source": [
    "#Load datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1acb498b-0205-4a0a-bfbe-a282cf117a28",
   "metadata": {},
   "outputs": [],
   "source": [
    "sal_df=pd.read_csv(r\"C:\\Users\\St.law\\eraaa_assignments\\sales_data.csv\")\n",
    "cus_df=pd.read_csv(r\"C:\\Users\\St.law\\eraaa_assignments\\customer_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7684889b-2e85-4667-b662-b3d739250c12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(  invoice_no customer_id  category  quantity    price invoice_date  \\\n",
       " 0    I138884     C241288  Clothing         5  1500.40   05-08-2022   \n",
       " 1    I317333     C111565     Shoes         3  1800.51   12-12-2021   \n",
       " 2    I127801     C266599  Clothing         1   300.08   09-11-2021   \n",
       " 3    I173702     C988172     Shoes         5  3000.85   16-05-2021   \n",
       " 4    I337046     C189076     Books         4    60.60   24-10-2021   \n",
       " \n",
       "     shopping_mall  \n",
       " 0          Kanyon  \n",
       " 1  Forum Istanbul  \n",
       " 2       Metrocity  \n",
       " 3    Metropol AVM  \n",
       " 4          Kanyon  ,\n",
       "   customer_id  gender   age payment_method\n",
       " 0     C241288  Female  28.0    Credit Card\n",
       " 1     C111565    Male  21.0     Debit Card\n",
       " 2     C266599    Male  20.0           Cash\n",
       " 3     C988172  Female  66.0    Credit Card\n",
       " 4     C189076  Female  53.0           Cash)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal_df.head(),cus_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc17719e-f186-417e-beb0-8bbe5c50c38f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "5086018d-1172-46cd-8165-a4d7db7a00d1",
   "metadata": {},
   "source": [
    "#---------Data Analysis----------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6593eba3-2227-4ef5-9ba1-746c9dfee807",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('sales data shape :', (99457, 7))"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"sales data shape :\", sal_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fa45321e-e666-485a-a24f-cb314f8c33f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('customer data shape :', (99457, 4))"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"customer data shape :\", cus_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "16362793-093e-4ce3-9269-e8a329541131",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 99457 entries, 0 to 99456\n",
      "Data columns (total 7 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   invoice_no     99457 non-null  object \n",
      " 1   customer_id    99457 non-null  object \n",
      " 2   category       99457 non-null  object \n",
      " 3   quantity       99457 non-null  int64  \n",
      " 4   price          99457 non-null  float64\n",
      " 5   invoice_date   99457 non-null  object \n",
      " 6   shopping_mall  99457 non-null  object \n",
      "dtypes: float64(1), int64(1), object(5)\n",
      "memory usage: 5.3+ MB\n"
     ]
    }
   ],
   "source": [
    "sal_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ce4cc56d-bcb1-4ac6-bca7-1dfbe8e6ad5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 99457 entries, 0 to 99456\n",
      "Data columns (total 4 columns):\n",
      " #   Column          Non-Null Count  Dtype  \n",
      "---  ------          --------------  -----  \n",
      " 0   customer_id     99457 non-null  object \n",
      " 1   gender          99457 non-null  object \n",
      " 2   age             99338 non-null  float64\n",
      " 3   payment_method  99457 non-null  object \n",
      "dtypes: float64(1), object(3)\n",
      "memory usage: 3.0+ MB\n"
     ]
    }
   ],
   "source": [
    "cus_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "3ae0b1b8-e5be-4e5e-b0c9-16fd0e8b6c99",
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
       "      <th>quantity</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>99457.000000</td>\n",
       "      <td>99457.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.003429</td>\n",
       "      <td>689.256321</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.413025</td>\n",
       "      <td>941.184567</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>5.230000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>45.450000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>203.300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>1200.320000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>5250.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           quantity         price\n",
       "count  99457.000000  99457.000000\n",
       "mean       3.003429    689.256321\n",
       "std        1.413025    941.184567\n",
       "min        1.000000      5.230000\n",
       "25%        2.000000     45.450000\n",
       "50%        3.000000    203.300000\n",
       "75%        4.000000   1200.320000\n",
       "max        5.000000   5250.000000"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal_df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "18cfca26-cecd-434e-95e5-3d118505a95d",
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
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>99338.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>43.425859</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>14.989400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>18.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>30.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>43.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>56.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>69.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age\n",
       "count  99338.000000\n",
       "mean      43.425859\n",
       "std       14.989400\n",
       "min       18.000000\n",
       "25%       30.000000\n",
       "50%       43.000000\n",
       "75%       56.000000\n",
       "max       69.000000"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cus_df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7fd90d73-5fa8-43e5-9373-200e5ec21508",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "invoice_no        object\n",
       "customer_id       object\n",
       "category          object\n",
       "quantity           int64\n",
       "price            float64\n",
       "invoice_date      object\n",
       "shopping_mall     object\n",
       "dtype: object"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal_df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9ffdba58-37e8-460d-a8d6-36ddf73f8df3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "customer_id        object\n",
       "gender             object\n",
       "age               float64\n",
       "payment_method     object\n",
       "dtype: object"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cus_df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "52ca3a0e-69e6-4f32-9047-f858520ac238",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal_df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2775a7dd-06c2-456b-95d6-6b86553e8c74",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cus_df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "902d7b40-720d-49e6-bacd-c3d5235a2b30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "invoice_no       0\n",
       "customer_id      0\n",
       "category         0\n",
       "quantity         0\n",
       "price            0\n",
       "invoice_date     0\n",
       "shopping_mall    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d93cc044-32c2-4507-a59f-91eab1bc03d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "customer_id         0\n",
       "gender              0\n",
       "age               119\n",
       "payment_method      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cus_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f29952b-f4c0-4b6d-b7b7-f61af78e9dfa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "4aba186f-d8da-4807-a889-bcdb7b8fbe81",
   "metadata": {},
   "source": [
    "#-----------Handle Missig age------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "701b4f82-9a48-4549-be63-931cf7a1546e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(43.0)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cus_df[\"age\"].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "bda27f37-1e6b-438c-80d4-7de8e1166dcf",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\St.law\\AppData\\Local\\Temp\\ipykernel_4660\\1429039889.py:1: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  cus_df[\"age\"].fillna(cus_df[\"age\"].median(),inplace=True)\n"
     ]
    }
   ],
   "source": [
    "cus_df[\"age\"].fillna(cus_df[\"age\"].median(),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1aed660f-09a2-42ae-b100-bc340e57a39d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "customer_id       0\n",
       "gender            0\n",
       "age               0\n",
       "payment_method    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cus_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed3ef1e2-d1cf-41f2-a6cc-470aefbef7b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "b316a305-f48d-4a3e-9c7e-79014cab67d0",
   "metadata": {},
   "source": [
    "#------------convert invoice_date to datetime data type-------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "e8e81302-f7f0-417f-b7a9-33bb9d0722f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        05-08-2022\n",
       "1        12-12-2021\n",
       "2        09-11-2021\n",
       "3        16-05-2021\n",
       "4        24-10-2021\n",
       "            ...    \n",
       "99452    21-09-2022\n",
       "99453    22-09-2021\n",
       "99454    28-03-2021\n",
       "99455    16-03-2021\n",
       "99456    15-10-2022\n",
       "Name: invoice_date, Length: 99457, dtype: object"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal_df['invoice_date']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8255d9d0-e933-4ac1-b475-34c77cce19b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "sal_df[\"invoice_date\"]=pd.to_datetime(sal_df[\"invoice_date\"].astype(str).str.strip(),errors=\"coerce\",dayfirst=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "26f27d86-7ce6-44d4-bf26-097742d99707",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "invoice_no               object\n",
       "customer_id              object\n",
       "category                 object\n",
       "quantity                  int64\n",
       "price                   float64\n",
       "invoice_date     datetime64[ns]\n",
       "shopping_mall            object\n",
       "dtype: object"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sal_df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1992a0c0-5aac-4cf9-93c3-1de3a8d89478",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "7d497b42-b3a1-437f-ae7b-443411341cdf",
   "metadata": {},
   "source": [
    "#------------merge sales and customer data----------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "33297a61-adc7-4c11-a779-7fec64b1d67c",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged=pd.merge(sal_df,cus_df,on=\"customer_id\",how=\"left\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "beb1866a-d549-4419-b531-da333dd6e2b0",
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
       "    shopping_mall  gender   age payment_method  total_sales age_group  \n",
       "0          Kanyon  Female  28.0    Credit Card      7502.00     20-29  \n",
       "1  Forum Istanbul    Male  21.0     Debit Card      5401.53     20-29  \n",
       "2       Metrocity    Male  20.0           Cash       300.08      Teen  \n",
       "3    Metropol AVM  Female  66.0    Credit Card     15004.25       40+  \n",
       "4          Kanyon  Female  53.0           Cash       242.40       40+  "
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5d8a6e2-5fa0-4621-9bce-6a65ee0b8acb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "60607683-356a-467f-b5f1-141d1bb06ac9",
   "metadata": {},
   "source": [
    "#-----------add some new columns/features------------"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5578a821-cd44-4bc4-bb13-24cc3ba4ab29",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true
   },
   "source": [
    "#---------1. Total sales----------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "7f3341a8-1d9c-4d00-affe-b3e89bc8a53c",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged[\"total_sales\"]=merged[\"quantity\"]*merged[\"price\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aec4efda-c91c-4473-93b9-f29d4269e8c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "660b7fed-2371-4050-a3a4-6d27bb2aae61",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "1056b1e2-f50c-4d12-a510-b8ff8adddf2d",
   "metadata": {},
   "source": [
    "#------------2. age in groups ----------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "64ecec22-ceba-4060-b4ad-da80780a1de1",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged[\"age_group\"]=pd.cut(\n",
    "    merged[\"age\"],\n",
    "    bins=[0, 20, 30, 40, 100],\n",
    "    labels=[\"Teen\", \"20-29\", \"30-39\", \"40+\"]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53dd2dab-7e3d-4596-a40d-c4a9d8e3cc8c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "f2cc65c2-8137-4d9d-9b4a-87956ea3901c",
   "metadata": {},
   "source": [
    "#--------3. Extract year, month, day name-------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "be76ecdf-bf69-4984-b4b5-0888836b0084",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged[\"year\"]=pd.DatetimeIndex(merged[\"invoice_date\"]).year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "234dda75-1957-46cf-8b52-ab5c1f5e507e",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged[\"month\"]=pd.DatetimeIndex(merged[\"invoice_date\"]).month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "9c318da1-0e89-4fd5-8c47-0c23ea7e6282",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged[\"day_name\"]=pd.to_datetime(merged[\"invoice_date\"]).dt.day_name()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "e0d9b000-8bb6-4503-bd56-5c056188d1f3",
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
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "1cee8c10-2732-44a4-aeb7-3d298ac7b180",
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
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34e079aa-822a-4fa4-9fc7-061c2f112dd8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "dbbc23f2-104b-4e0a-bbe9-fadab2389e2a",
   "metadata": {},
   "source": [
    "#-------------save cleaned data-----------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "fe199916-943b-4ee7-a631-1980e380dd71",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged.to_csv(r\"C:\\pyythonn\\Assignment 1\\cleaned_data.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bbaa14e-688f-4533-b253-dfd4510d7d84",
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
