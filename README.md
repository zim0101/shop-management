# shop-management

File Structure:
├── app
│   ├── constants.py
│   ├── __init__.py
│   ├── utils
│   │   ├── crypto.py
│   │   ├── __init__.py
│   └── views.py
├── auth
│   ├── auth.py
│   ├── daos.py
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   ├── services.py
│   ├── validations.py
│   └── wrappers.py
├── config.py
├── employee
│   ├── daos.py
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── views.py
├── product
│   ├── daos
│   │   ├── category_dao.py
│   │   ├── __init__.py
│   │   ├── product_dao.py
│   │   └── subcategory_dao.py
│   ├── __init__.py
│   ├── models
│   │   ├── category.py
│   │   ├── __init__.py
│   │   ├── product.py
│   │   ├── product_variation.py
│   │   └── subcategory.py
│   ├── schemas
│   │   ├── category_schema.py
│   │   ├── __init__.py
│   │   ├── product_schema.py
│   │   ├── product_variation_schema.py
│   │   └── subcategory_schema.py
│   ├── services
│   │   ├── category_service.py
│   │   ├── __init__.py
│   │   ├── product_service.py
│   │   ├── product_variation_service.py
│   │   └── subcategory_service.py
│   ├── validations
│   │   ├── category_validation.py
│   │   ├── __init__.py
│   │   ├── product_validation.py
│   │   ├── product_variation_validation.py
│   │   └── subcategory_validation.py
│   └── views
│       ├── category_views.py
│       ├── __init__.py
│       ├── product_views.py
│       └── subcategory_views.py
├── requirements.txt
├── run.py
└── shop
    ├── daos
    │   ├── __init__.py
    │   ├── shop_category_dao.py
    │   └── shop_dao.py
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   ├── shop_category.py
    │   └── shop.py
    ├── schemas
    │   ├── __init__.py
    │   ├── shop_category_schema.py
    │   └── shop_schema.py
    ├── services
    │   ├── __init__.py
    │   ├── shop_category_service.py
    │   └── shop_service.py
    ├── validations
    │   ├── __init__.py
    │   ├── shop_category_validation.py
    │   └── shop_validation.py
    └── views
        ├── __init__.py
        ├── shop_category_view.py
        └── shop_view.py
