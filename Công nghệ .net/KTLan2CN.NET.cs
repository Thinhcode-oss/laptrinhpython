using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace QLThietBiApp
{
    public partial class Form1 : Form
    {
        // Chuỗi kết nối (Thay đổi tên Server cho phù hợp với máy của bạn)
        string connectionString = @"Data Source=.\SQLEXPRESS;Initial Catalog=QLThietBi;Integrated Security=True";
        SqlConnection conn;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            conn = new SqlConnection(connectionString);
            
            [cite_start]// g) Hiển thị ngày giờ bắt đầu của Form [cite: 61]
            this.Text = "Bắt đầu lúc: " + DateTime.Now.ToString("G");
            
            [cite_start]// a) Con trỏ đặt vào ô Mã Thiết bị [cite: 50]
            txtMaTB.Focus();

            LoadDataGridView();
            LoadTreeView();
            StartTimers();
        }

        #region Xử lý Dữ liệu

        [cite_start]// a) Lấy dữ liệu từ Database đưa lên DataGridView [cite: 52]
        private void LoadDataGridView()
        {
            try
            {
                if (conn.State == ConnectionState.Closed) conn.Open();
                
                // JOIN để lấy thuế suất từ bảng Loai phục vụ tính toán
                string query = "SELECT T.*, L.Ten as TenLoai, L.Thue FROM ThietBi T JOIN Loai L ON T.MaLoai = L.MaLoai";
                SqlDataAdapter da = new SqlDataAdapter(query, conn);
                DataTable dt = new DataTable();
                da.Fill(dt);
                dgvThietBi.DataSource = dt;

                TinhToanThongKe(dt);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi tải dữ liệu: " + ex.Message);
            }
            finally { conn.Close(); }
        }

        [cite_start]// b) Tính toán Tổng giá mua và Trung bình 
        private void TinhToanThongKe(DataTable dt)
        {
            double tongGiaMua = 0;
            int n = dt.Rows.Count;
            int phi = 100; // Phi cố định 

            foreach (DataRow row in dt.Rows)
            {
                int donGia = Convert.ToInt32(row["DonGia"]);
                int thueSuat = Convert.ToInt32(row["Thue"]);
                
                [cite_start]// Công thức: Tiền thuế = (Đơn giá + Phi) * (Tỷ lệ / 100) 
                double tienThue = (donGia + phi) * (thueSuat / 100.0);
                tongGiaMua += (donGia + tienThue);
            }

            txtTongGiaMua.Text = tongGiaMua.ToString("N0");
            txtTrungBinh.Text = n > 0 ? (tongGiaMua / n).ToString("N2") : "0";
        }

        [cite_start]// c) TreeView để chọn loại 
        private void LoadTreeView()
        {
            tvLoai.Nodes.Clear();
            if (conn.State == ConnectionState.Closed) conn.Open();
            SqlCommand cmd = new SqlCommand("SELECT MaLoai, Ten FROM Loai", conn);
            SqlDataReader dr = cmd.ExecuteReader();
            while (dr.Read())
            {
                TreeNode node = new TreeNode(dr["Ten"].ToString());
                node.Tag = dr["MaLoai"].ToString();
                tvLoai.Nodes.Add(node);
            }
            conn.Close();
        }

        private void tvLoai_AfterSelect(object sender, TreeViewEventArgs e)
        {
            txtLoaiSelected.Text = e.Node.Text;
            txtLoaiSelected.Tag = e.Node.Tag; // Lưu MaLoai vào Tag
        }

        #endregion

        #region Chức năng nghiệp vụ

        [cite_start]// d) Nút Nhập mới (Thêm thiết bị) [cite: 57]
        private void btnNhapMoi_Click(object sender, EventArgs e)
        {
            [cite_start]// Kiểm tra rỗng [cite: 51]
            if (string.IsNullOrWhiteSpace(txtMaTB.Text) || string.IsNullOrWhiteSpace(txtTenTB.Text))
            {
                MessageBox.Show("Vui lòng nhập đầy đủ thông tin!");
                return;
            }

            try
            {
                conn.Open();
                string sql = "INSERT INTO ThietBi VALUES(@ma, @ten, @gia, @loai)";
                SqlCommand cmd = new SqlCommand(sql, conn);
                cmd.Parameters.AddWithValue("@ma", txtMaTB.Text);
                cmd.Parameters.AddWithValue("@ten", txtTenTB.Text);
                cmd.Parameters.AddWithValue("@gia", txtDonGia.Text);
                cmd.Parameters.AddWithValue("@loai", txtLoaiSelected.Tag ?? 1);
                
                cmd.ExecuteNonQuery();
                LoadDataGridView(); // Cập nhật lại Grid và Thống kê [cite: 57]
            }
            catch (Exception ex) { MessageBox.Show(ex.Message); }
            finally { conn.Close(); }
        }

        [cite_start]// i) Lưu ra file txt [cite: 68]
        private void btnLuuFile_Click(object sender, EventArgs e)
        {
            using (StreamWriter sw = new StreamWriter("DanhSachThietBi.txt"))
            {
                sw.WriteLine("MTB\tTTB\tDonGia\tMaLoai");
                foreach (DataGridViewRow row in dgvThietBi.Rows)
                {
                    if (!row.IsNewRow)
                    {
                        sw.WriteLine($"{row.Cells[0].Value}\t{row.Cells[1].Value}\t{row.Cells[2].Value}\t{row.Cells[3].Value}");
                    }
                }
            }
            [cite_start]MessageBox.Show("Đã lưu file thành công!"); [cite: 69]
        }

        [cite_start]// j) Nút Thoát [cite: 70]
        private void btnThoat_Click(object sender, EventArgs e)
        {
            DialogResult dr = MessageBox.Show("Bạn có chắc chắn muốn thoát?", "Xác nhận", MessageBoxButtons.YesNo);
            [cite_start]if (dr == DialogResult.Yes) Application.Exit(); [cite: 71]
        }

        #endregion

        #region Xử lý Thời gian

        private void StartTimers()
        {
            Timer timerClock = new Timer();
            timerClock.Interval = 1000;
            timerClock.Tick += (s, e) => {
                [cite_start]// g) Thời gian hiện hành góc trái 
                txtCurrentTime.Text = DateTime.Now.ToString("HH:mm:ss");

                [cite_start]// g) Tự động tăng giây và cập nhật DB [cite: 65]
                int currentSec = int.Parse(txtTimerCounter.Text);
                int limitSec = int.TryParse(txtTimerLimit.Text, out int res) ? res : 0;

                currentSec++;
                if (limitSec > 0 && currentSec >= limitSec)
                {
                    currentSec = 0;
                    LoadDataGridView(); // Cập nhật từ DB [cite: 65]
                    [cite_start]MessageBox.Show("Tự động cập nhật dữ liệu thành công!"); [cite: 66]
                }
                txtTimerCounter.Text = currentSec.ToString();
            };
            timerClock.Start();
        }

        #endregion
    }
}