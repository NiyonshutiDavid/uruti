```mermaid
erDiagram
    Profile {
        string UserEmail PK
        string Username
        string Names
        string ProfilePicture
        string Role
        string[] Followers
        string[] Following
    }

    Post {
        string PostID PK
        string PosterID FK
        string Description
        string DateCreated
        string ImageUrl
        string TimesShared
    }

    Comment {
        string CommentID PK
        string PostID FK
        string CommenterID FK
        string Message
    }

    Likes {
        string LikeID PK
        string PostID FK
        string LikerID FK
    }

    Product {
        string ProductID PK
        string Name
        string Price
        string Category
        string imageUrl
        string inStock
    }

    Order {
        string OrderID PK
        string ProductID FK
        string UserId FK
        string Quantity
        string Price
        string OrderStatus
        string timeStamp
    }

    Cart {
        string CartID PK
        string BuyerID FK
        string[] OrderID
        string TotalPrice
    }

    Payment {
        string PaymentID PK
        string PayerID FK
        string OrderID FK
        string PaymentAmount
        string TimeStamp
    }

    Bill {
        string BillID PK
        string TotalPrice
        string[] Items
        string TimeStamp
    }

    Message {
        string CollectionID PK
        string FromUserId FK
        string ToUserId FK
        string Message
        string Status
        string TimeStamp
    }

    Profile ||--o{ Post : "PosterID"
    Profile ||--o{ Comment : "CommenterID"
    Post ||--o{ Comment : "PostID"
    Post ||--o{ Likes : "PostID"
    Profile ||--o{ Likes : "LikerID"
    Product ||--o{ Order : "ProductID"
    Profile ||--o{ Order : "UserId"
    Profile ||--o{ Cart : "BuyerID"
    Order ||--o{ Payment : "OrderID"
    Profile ||--o{ Payment : "PayerID"
    Profile ||--o{ Message : "FromUserId"
    Profile ||--o{ Message : "ToUserId"
