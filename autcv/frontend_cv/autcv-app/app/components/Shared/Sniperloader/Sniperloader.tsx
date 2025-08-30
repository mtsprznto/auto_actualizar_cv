// app\components\Shared\SnipperLoader\Sniperloader.tsx
export function SniperLoading() {
  return (
    <div className="flex items-center justify-center h-screen bg-white dark:bg-gray-900">
      <div className="relative">
        <div
          className="w-16 h-16 border-4 border-gray-300 rounded-full animate-spin border-t-blue-600"
          aria-label="Cargando sesión segura"
        ></div>
      </div>
    </div>
  );
}
