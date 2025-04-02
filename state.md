```mermaid
graph TD
    A[runApp()] -->|Wraps app with| B[MultiProvider]
    B -->|Provides state| C[ChangeNotifierProvider: AuthNotifier]
    B -->|Provides state| D[ChangeNotifierProvider: ProfileCompletionNotifier]
    C -->|Manages| E[Authentication State]
    D -->|Manages| F[Profile Completion State]
    B --> G[MyApp()]
