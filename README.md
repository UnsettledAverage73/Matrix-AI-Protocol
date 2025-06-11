# Lending App

A React Native application for loan prediction using machine learning.

## Features

- Loan application form
- Real-time loan prediction
- Integration with ML model API
- User-friendly interface

## Prerequisites

- Node.js (v14 or newer)
- npm or yarn
- React Native development environment set up
- Android Studio (for Android development)
- Xcode (for iOS development, macOS only)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd LendingApp
```

2. Install dependencies:
```bash
npm install
```

3. Start the Metro bundler:
```bash
npm start
```

4. Run the application:

For Android:
```bash
npm run android
```

For iOS:
```bash
npm run ios
```

## Project Structure

```
LendingApp/
├── src/
│   ├── components/     # Reusable components
│   ├── screens/        # Screen components
│   ├── services/       # API services
│   └── utils/          # Utility functions
├── App.js             # Main application component
└── package.json       # Project dependencies
```

## API Integration

The app integrates with a FastAPI backend for loan prediction. Make sure the API server is running at `http://127.0.0.1:8000` before testing the application.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.